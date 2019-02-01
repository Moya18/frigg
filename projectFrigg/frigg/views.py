from django.shortcuts import get_object_or_404, render
import os, sys, re, time
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta, datetime

from .models import Quote, Job

from .forms import QuoteForm, ClientForm, ApproveForm

def index(request):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    #OR
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'frigg/index.html', {})

def fillQuoteForm(request):
    return render(request, 'frigg/Quote_Form.html', {})

def fillClientForm(request):
    return render(request, 'frigg/Client_Form.html', {})

def approveQuote(request):
    #GETTING READY...
    form = ApproveForm(request.POST)
    form.is_valid()
    form = form.clean()
    quote = Quote.objects.get(pk = form['quoteID'])
    #FILL FIELDS
    quote.status = 'approved'
    for job in Job.objects.filter(key = quote.key):
        job.quote_id = quote
        job.date_time_code = Quote.objects.get(pk=form['quoteID']).date_time_code
        job.status = 'pending'
        job.save()
        quote.job_number = str(int(quote.job_number) + 1)

    #SAVE
    quote.save()

    os.system("python frigg\pdf\JobMake.py")

    return render(request, 'frigg/thanks.html', {})

def createQuote(request):
    #GETTING READY...
    form = QuoteForm(request.POST, request.FILES)
    form.is_valid()
    form = form.clean()
    quote, created = Quote.objects.get_or_create(key=form['hidden'])
    job = Job()

    #FILL QUOTE FIELDS
    if(created):
        quote.key = form['hidden']
        quote.client = form['client']
        quote.date_time_code = form['date']
        quote.total_price = form['showCost']
        quote.job_number = 0
        quote.status = 'on hold'
    
    #FILL JOB FIELDS
    job.client = form['client']
    job.date_time_code = form['date']
    job.material = form['material']
    job.layers = form['layerThickness']
    job.infill = form['infill']
    job.supports = form['supports']
    job.speed = form['speed']
    job.print_time = form['time']
    job.weight = form['weight']
    job.number_copies = form['quantity']
    job.status = 'on hold'
    job.key = form['hidden']

    #CREATE DIRECTORY FOR FILES
    try:
        os.mkdir('frigg/job_models/' + job.client)
        os.mkdir('frigg/job_models/' + job.client + '/model')
        os.mkdir('frigg/job_models/' + job.client + '/model_orientation')
    except OSError:
        pass
    #END

    path = 'frigg/job_models/' + job.client + '/model/' + request.FILES['printFile1'].name
    handle_uploaded_file(request.FILES['printFile1'], path)
    job.model_path = path

    path = 'frigg/job_models/' + job.client + '/model_orientation/' + request.FILES['orientationFile1'].name
    handle_uploaded_file(request.FILES['orientationFile1'], path)
    job.model_orientation_path = path

    #SAVE
    quote.save()
    job.save()

    #DELETE NOT USEFUL QUOTES AND CALCULATE JOB NUMBER
    quotesCreated = Quote.objects.filter(key = form['hidden'])
    iterQuotesCreated = iter(quotesCreated)
    if(len(quotesCreated) > 1):
        next(iterQuotesCreated)
        for quoteCreated in iterQuotesCreated:
            quoteCreated.delete()

    #SEND CONFIRMATION EMAIL
    #send_email()

    #run sheets file TEST
    os.system("python frigg\sheets\GoogleTest.py")
    os.system("python frigg\pdf\QuoteMake.py")

    return render(request, 'frigg/thanks.html', {})

def createClient(request):
    #GETTING READY...
    form = ClientForm(request.POST, request.FILES)
    client = Client()
    form.is_valid()
    form = form.clean()

    #FILL FIELDS
    client.name = form['name']
    client.company = form['company']
    client.email = form['email']
    client.phone_number = form['telephone']
    client.rfc = form['rfc']
    client.address_line1 = form['addressLine1']
    client.address_line2 = form['addressLine2']
    client.city = form['city']
    client.zip = form['zip']

    #SAVE
    client.save()

    return render(request, 'frigg/thanks.html', {})

def getQuotes(request):
    quote_list = Quote.objects.all()
    context = {'quote_list': quote_list}
    return render(request, 'frigg/Quote_List.html', context)

def getJobs(request):
    job_list = Job.objects.all()
    context = {'job_list': job_list}
    return render(request, 'frigg/Job_List.html', context)

def handle_uploaded_file(f, path):
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def send_email():
    send_mail(
        'Subject here',
        'Here is the message.',
        '0197221@up.edu.mx',
        ['0197221@up.edu.mx'],
        fail_silently=False,
    )

def createTemporaryLink():
    try:
        testArg = re.match('s3:\/\/', sys.argv[1])
    except:
        print("usage: " + sys.argv[0] + " s3_object ttl_in_sec")
        sys.exit(1)
    if not testArg:
        print
        "need a valid s3 object as arg"
        sys.exit(1)

    try:
        sys.argv[2]
        expTime = int(sys.argv[2])
    except:
        expTime = 60

    (bucket, key) = re.split('/', re.sub('^s3:\/\/', '', sys.argv[1]), maxsplit=1)

    testKey = re.match('\w', key)
    if not testKey:
        print("something wrong with this url - I have a key of: " + key + " - bailing")
        sys.exit(1)

    from boto.s3.connection import S3Connection
    s3 = S3Connection()
    url = s3.generate_url(expTime, 'GET', bucket=bucket, key=key)
    print(url)
