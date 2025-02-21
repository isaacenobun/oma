from django.core.mail import send_mail
    
def send_oma_mail():
    print ('mail sent')
    send_mail(
        'Good morning',
        'This is a test email',
        'isaacenobun@gmail.com',
        ['ienobun412@stu.ui.edu.ng', 'isaacenobun@gmail.com'],
    )