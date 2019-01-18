from django.shortcuts import get_object_or_404, render
import os, sys, re
from django.core.mail import send_mail
from django.conf import settings

from .models import Quote, Client

from .forms import QuoteForm, ClientForm

def index(request):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    #OR
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'frigg/index.html', {})

def quoteList(request):
    #quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'frigg/Quote_List.html', {})

def fillQuoteForm(request):
    return render(request, 'frigg/Quote_Form.html', {})

def fillClientForm(request):
    return render(request, 'frigg/Client_Form.html', {})

def createQuote(request):

    #GETTING READY...
    form = QuoteForm(request.POST, request.FILES)
    quote = Quote()
    form.is_valid()
    form = form.clean()

    #FILL FIELDS
    quote.client_id = Client.objects.get(name=form['client'])
    quote.company = form['client']
    quote.date_time_code = form['date']

    #CREATE DIRECTORY FOR FILES
    try:                 #MOST CHANGE TO quote.user
        os.mkdir('frigg/quote_models/' + quote.company)
        os.mkdir('frigg/quote_models/' + quote.company + '/model')
        os.mkdir('frigg/quote_models/' + quote.company + '/model_orientation')
    except OSError:
        pass
    #END

    path = 'frigg/quote_models/' + quote.company + '/model/' + request.FILES['printFile1'].name
    handle_uploaded_file(request.FILES['printFile1'], path)
    quote.model_path = path
    path = 'frigg/quote_models/' + quote.company + '/model_orientation/' + request.FILES['orientationFile1'].name
    handle_uploaded_file(request.FILES['orientationFile1'], path)
    quote.model_orientation_path = path
    quote.material = form['material']
    quote.status = 'pending'

    #SAVE
    quote.save()

    #SEND CONFIRMATION EMAIL
    #send_email()

    #run sheets file TEST
    os.system("python frigg\sheets\GoogleTest.py")

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