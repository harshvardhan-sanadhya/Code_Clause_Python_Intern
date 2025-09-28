import mysql.connector
import random
import string
import socket
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='harshvardhan',
    database='shorter_py'
)
cursor=conn.cursor()
while True:
    def user_analysis(userid):
        """Show analytics for all URLs of the logged-in user."""
        sql = """
            SELECT u.short_code, u.original_url, COUNT(a.id) AS total_clicks, 
                MAX(a.clicked_at) AS last_clicked
            FROM urls u
            LEFT JOIN analytics a ON u.id = a.url_id
            WHERE u.user_id = %s
            GROUP BY u.id
        """
        cursor.execute(sql, (userid,))
        results = cursor.fetchall()

        if results:
            print("\n📊 Your URL Analytics:\n")
            for short_code, original_url, total_clicks, last_clicked in results:
                print(f"Short code: {short_code} | URL: {original_url}")
                print(f"Total Clicks: {total_clicks} | Last Clicked: {last_clicked}\n")
        else:
            print("You haven’t added any URLs yet.")

    def short_code_generator(length=6):
        while True:
            short_code=''.join(random.choices(string.ascii_letters + string.digits,k=length))
            sql="select id from urls where short_code=%s"
            cursor.execute(sql,(short_code,))
            result=cursor.fetchone()
            if not result:
                return short_code   

    def open_url(userid):
        input_short=input("Enter your short code here : ")

        sql="select id, original_url from urls where user_id =%s and short_code = %s"
        values=(userid,input_short)
        cursor.execute(sql,values)
        result=cursor.fetchone()

        if result:
            url_id,original_url=result
            print(f"your long url is this: {original_url}")
            ip_address=socket.gethostbyname(socket.gethostname())
            user_agent="Python-CLI"

            sql_log="insert into analytics (url_id,ip_address,user_agent) values (%s,%s,%s)"
            cursor.execute(sql_log,(url_id,ip_address,user_agent))
            conn.commit()

            user_analysis(userid)
        else:
            print("No url found")

    def add_url(userid):
        original_url=input("Enter your url here : ")
        short_code=short_code_generator()
        sql="insert into urls (user_id,original_url,short_code) values(%s,%s,%s)"
        values=(userid,original_url,short_code)
        cursor.execute(sql,values)
        conn.commit()
        print(f" Your short url code is :{short_code}")

    def options(userid):
        print("Enter Your Choice Please")
        print("Write Add  for adding the  URL")
        print("Write Open for opening the URL")
        option_input=input("Enter your choice here : ").strip()
        if option_input=='add':
            add_url(userid)
        elif option_input=='open':
            open_url(userid)
        else:
            print("Wrong Choice")
        

    def signup():
        print("Fill the information below : ")
        usern=input("Enter your username here : " )
        passn=input("Enter your password here : ")
        emailn=input("Enter your email here : ")

        sql="insert into users (username,email,password_hash) values (%s,%s,%s)"
        values=(usern,emailn,passn)
        cursor.execute(sql,values)
        conn.commit()
        print("User added Successfully !")
        

        userid=cursor.lastrowid
        options(userid)


    def signin():
        print("Fill the information below : ")
        useri=input("Enter your username here : " ).strip()
        passi=input("Enter your password here : ").strip()

        sql="select id,password_hash from users where username = %s"
        values=(useri,)
        cursor.execute(sql,values)
        entered_pass_from_db=cursor.fetchone()

        if entered_pass_from_db and  passi == entered_pass_from_db[1]:
            print("Login Successfull !")
            userid=entered_pass_from_db[0]
            options(userid)
        else:
            print("Wrong id poass")

    print("\n \t\t\tWelcome to the url shortner")
    print("Select your options")
    print("1. Sign Up")
    print("2. Sign In")
    input_selector=input("Enter Here : ").strip()


    if input_selector.lower() == "sign up":
        signup()
    elif input_selector.lower()=="sign in":
        signin()
    else:
        print("wrong choice")
