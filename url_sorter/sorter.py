import mysql.connector
import random
import string
import socket

# Database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='harshvardhan',
    database='shorter_py'
)
cursor = conn.cursor()


# ================== Functions ==================

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
    """Generate a unique short code for the URL."""
    while True:
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        sql = "SELECT id FROM urls WHERE short_code=%s"
        cursor.execute(sql, (short_code,))
        result = cursor.fetchone()
        if not result:
            return short_code


def open_url(userid):
    input_short = input("Enter your short code here : ")

    sql = "SELECT id, original_url FROM urls WHERE user_id =%s AND short_code = %s"
    values = (userid, input_short)
    cursor.execute(sql, values)
    result = cursor.fetchone()

    if result:
        url_id, original_url = result
        print(f"Your long URL is this: {original_url}")

        ip_address = socket.gethostbyname(socket.gethostname())
        user_agent = "Python-CLI"

        sql_log = "INSERT INTO analytics (url_id,ip_address,user_agent) VALUES (%s,%s,%s)"
        cursor.execute(sql_log, (url_id, ip_address, user_agent))
        conn.commit()

        user_analysis(userid)
    else:
        print("No URL found")


def add_url(userid):
    original_url = input("Enter your URL here : ")
    short_code = short_code_generator()
    sql = "INSERT INTO urls (user_id,original_url,short_code) VALUES(%s,%s,%s)"
    values = (userid, original_url, short_code)
    cursor.execute(sql, values)
    conn.commit()
    print(f" Your short URL code is : {short_code}")


def options(userid):
    print("Enter Your Choice Please")
    print("Write Add  for adding the  URL")
    print("Write Open for opening the URL")
    option_input = input("Enter your choice here : ").strip().lower()
    if option_input == 'add':
        add_url(userid)
    elif option_input == 'open':
        open_url(userid)
    else:
        print("Wrong Choice")


def signup():
    print("Fill the information below : ")
    usern = input("Enter your username here : ")
    passn = input("Enter your password here : ")
    emailn = input("Enter your email here : ")

    sql = "INSERT INTO users (username,email,password_hash) VALUES (%s,%s,%s)"
    values = (usern, emailn, passn)
    cursor.execute(sql, values)
    conn.commit()
    print("User added Successfully !")

    userid = cursor.lastrowid
    options(userid)


def signin():
    print("Fill the information below : ")
    useri = input("Enter your username here : ").strip()
    passi = input("Enter your password here : ").strip()

    sql = "SELECT id,password_hash FROM users WHERE username = %s"
    values = (useri,)
    cursor.execute(sql, values)
    entered_pass_from_db = cursor.fetchone()

    if entered_pass_from_db and passi == entered_pass_from_db[1]:
        print("Login Successful !")
        userid = entered_pass_from_db[0]
        options(userid)
    else:
        print("Wrong username or password")


# ================== Main Loop ==================
while True:
    print("\n \t\t\tWelcome to the URL Shortener")
    print("Select your options")
    print("1. Sign Up")
    print("2. Sign In")

    input_selector = input("Enter Here : ").strip().lower()

    if input_selector == "sign up" or input_selector == "1":
        signup()
    elif input_selector == "sign in" or input_selector == "2":
        signin()
    else:
        print("Wrong choice")

