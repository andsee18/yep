import psycopg2

def save_vacancies(vacancies):
    """
    Сохраняет вакансии в базу данных PostgreSQL.
    
    :param vacancies: Список словарей с данными о вакансиях.
    """
    conn = psycopg2.connect(
        dbname='hh_parser',
        user='hh_user',
        password='hh_password',
        host='db',
        port='5432'
    )
    cur = conn.cursor()
    for vacancy in vacancies:
        cur.execute(
            "INSERT INTO vacancies (title, link, company, location, salary) VALUES (%s, %s, %s, %s, %s)",
            (vacancy['title'], vacancy['link'], vacancy['company'], vacancy['location'], vacancy['salary'])
        )
    conn.commit()
    cur.close()
    conn.close()

def get_analytics():
    """
    Получает общее количество вакансий из базы данных PostgreSQL.
    
    :return: Общее количество вакансий.
    """
    conn = psycopg2.connect(
        dbname='hh_parser',
        user='hh_user',
        password='hh_password',
        host='db',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM vacancies")
    total_vacancies = cur.fetchone()[0]
    cur.close()
    conn.close()
    return total_vacancies