from django.shortcuts import get_object_or_404, render
import os, sys, re, time, json, codecs
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta, datetime

from .models import Quote, Job
from .forms import QuoteForm, ClientForm, ApproveForm
from .pdf import JobMake, QuoteMake
from .sheets import GoogleTest

def index(request):
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

    JobMake.run(quote.id, quote.date_time_code)

    return render(request, 'frigg/thanks.html', {})

def createQuote(request):
    data = json.loads(request.body)
    fields = 18
    job_number = int(len(data) / fields) #IMPORTANT!!! NUMBER OF FIELDS IN EACH FORM, CHANGE IF FIELDS ARE ADDED OR SUBSTRACTED
    print(job_number, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    #GETTING READY
    quote = Quote()
    
    client = data[1]['value']
    date = data[2]['value']
    hidden = data[13]['value']

    quote.client = client
    quote.date_time_code = date
    quote.date_approved = date #STILL NEEDS TO BE MODIFIED
    quote.date_due = date #STILL NEEDS TO BE MODIFIED
    quote.total_price = data[12]['value']
    quote.job_number = job_number
    quote.jobs_completed = 0
    quote.status = 'on hold'
    quote.key = hidden

    quote.save()

    for i in range(job_number):
        job = Job()
        x = i * fields #ITERATION NUMBER TO SEPARATE FORMS
        #ORDER OF FIELDS ARE IMPORTANT!!
        material = data[x + 3]['value']
        layerThickness = data[x + 4]['value']
        infill = data[x + 5]['value']
        supports = data[x + 6]['value']
        speed = data[x + 7]['value']
        print_time = data[x + 8]['value']
        weight = data[x + 9]['value']
        quantity = data[x + 10]['value']
        deliveryDate = data[x + 11]['value']
        cost = data[x + 12]['value']
        printFile = data[x + 14]['value'].split('\\')[-1]
        orientationFile = data[x + 15]['value'].split('\\')[-1]
        printFileData = data[x + 16]['value']
        orientationFileData = data[x + 17]['value']

        #CREATE DIRECTORY FOR FILES
        try:
            os.mkdir('frigg/quotes/')
        except OSError:
            pass
        try:
            os.mkdir('frigg/quotes/quote' + str(quote.id))
        except OSError:
            pass
        try:
            os.mkdir('frigg/quotes/quote' + str(quote.id) + '/' + client)
        except OSError:
            pass
        try:
            os.mkdir('frigg/quotes/quote' + str(quote.id) + '/' + client + '/pdf')
        except OSError:
            pass
        try:
            os.mkdir('frigg/quotes/quote' + str(quote.id) + '/' + client + '/jobs')
        except OSError:
            pass
        try:
            os.mkdir('frigg/quotes/quote' + str(quote.id) + '/' + client + '/jobs/job' + str(i))
        except OSError:
            pass
        try:
            os.mkdir('frigg/quotes/quote' + str(quote.id) + '/' + client + '/jobs/job' + str(i) + '/model')
        except OSError:
            pass
        try:
            os.mkdir('frigg/quotes/quote' + str(quote.id) + '/' + client + '/jobs/job' + str(i) + '/model_orientation')
        except OSError:
            pass
        #END

        model_path = 'frigg/quotes/quote' + str(quote.id) + '/' + client + '/jobs/job' + str(i) + '/model/' + printFile
        handle_uploaded_file(printFileData, model_path)
        model_orientation_path = 'frigg/quotes/quote' + str(quote.id) + '/' + client + '/jobs/job' + str(i) + '/model_orientation/' + orientationFile
        handle_uploaded_file(orientationFileData, model_orientation_path)

        job.client = client
        job.date_time_code = date
        job.model_path = model_path
        job.model_orientation_path = model_orientation_path
        job.material = material
        job.layers = layerThickness
        job.infill = infill
        job.supports = supports
        job.speed = speed
        job.print_time = print_time
        job.weight = weight
        job.number_copies = quantity
        job.date_due = date
        job.quote_id = quote
        job.status = 'on hold'
        job.key = hidden

        job.save()

    jobs = []
    printFile = data[14]['value'].split('\\')[-1]
    orientationFile = data[15]['value'].split('\\')[-1]
    cost = data[12]['value']
    quantity = data[10]['value']
    jobsCreated = Job.objects.filter(key = hidden)
    for job in jobsCreated:
        array = []
        array.append(job.material)
        array.append(job.layers)
        array.append("colour") #Not a field in DB yet
        array1 = []
        array2 = [printFile, int(cost), int(quantity)]
        array1.append(array2)
        array.append(array1)
        jobs.append(array)
    QuoteMake.run(quote.client, quote.id, quote.date_time_code, jobs)




    # #GETTING READY...
    # form = QuoteForm(request.POST, request.FILES)
    # form.is_valid()
    # form = form.clean()
    # quote, created = Quote.objects.get_or_create(key=form['hidden'])
    # job = Job()

    # #FILL QUOTE FIELDS
    # if(created):
    #     quote.key = form['hidden']
    #     quote.client = form['client']
    #     quote.date_time_code = form['date']
    #     quote.total_price = form['showCost']
    #     quote.job_number = form['jobs']
    #     quote.status = 'on hold'
    
    # #FILL JOB FIELDS
    # job.client = form['client']
    # job.date_time_code = form['date']
    # job.material = form['material']
    # job.layers = form['layerThickness']
    # job.infill = form['infill']
    # job.supports = form['supports']
    # job.speed = form['speed']
    # job.print_time = form['time']
    # job.weight = form['weight']
    # job.number_copies = form['quantity']
    # job.status = 'on hold'
    # job.key = form['hidden']

    # #CREATE DIRECTORY FOR FILES
    # try:
    #     os.mkdir('frigg/jobs/' + job.client)
    #     os.mkdir('frigg/jobs/' + job.client + '/model')
    #     os.mkdir('frigg/jobs/' + job.client + '/model_orientation')
    #     os.mkdir('frigg/jobs/' + job.client + '/pdf')
    # except OSError:
    #     pass
    # #END

    # path = 'frigg/jobs/' + job.client + '/model/' + request.FILES['printFile1'].name
    # handle_uploaded_file(request.FILES['printFile1'], path)
    # job.model_path = path

    # path = 'frigg/jobs/' + job.client + '/model_orientation/' + request.FILES['orientationFile1'].name
    # handle_uploaded_file(request.FILES['orientationFile1'], path)
    # job.model_orientation_path = path

    # #SAVE
    # quote.save()
    # job.save()

    # #DELETE NOT USEFUL QUOTES AND CALCULATE JOB NUMBER
    # quotesCreated = Quote.objects.filter(key = form['hidden'])
    # iterQuotesCreated = iter(quotesCreated)
    # if(len(quotesCreated) > 1):
    #     next(iterQuotesCreated)
    #     for quoteCreated in iterQuotesCreated:
    #         quoteCreated.delete()

    #SEND CONFIRMATION EMAIL
    #send_email()

    #run sheets file TEST
    #GoogleTest.run()
    # if(int(quote.job_number) == int(form['jobs'])):
    #     jobs = []
    #     jobsCreated = Job.objects.filter(key = form['hidden'])
    #     for job in jobsCreated:
    #         array = []
    #         array.append(job.material)
    #         array.append(job.layers)
    #         array.append("colour")
    #         array1 = []
    #         array2 = [request.FILES['printFile1'], int(form['showCost']), int(form['quantity'])]
    #         array1.append(array2)
    #         array.append(array1)
    #         jobs.append(array)
    #     QuoteMake.run(quote.client, quote.id, quote.date_time_code, jobs)
    # os.system("python frigg\sheets\GoogleTest.py")

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
    with codecs.open(path, 'wb+', encoding='UTF-8') as destination:
        #for chunk in f.chunks():
        destination.write(f)

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
