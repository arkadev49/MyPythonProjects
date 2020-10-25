from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# new_row = Table(string_field='This is string field!',
#                 date_field=datetime.strptime('01-24-2020', '%m-%d-%Y').date())
#
# session.add(new_row)
# session.commit()

# rows = session.query(Table).all()
# print(rows)
# first_row = rows[0]
#
# print(first_row.string_field)
# print(first_row.id)
# print(first_row)

while True:
    print("\n1) Today's tasks")
    print("2) Week's tasks")
    print('3) All tasks')
    print('4) Missed tasks')
    print('5) Add task')
    print('6) Delete task')
    print('0) Exit')
    choice = int(input())
    print()
    if choice == 1:
        print('Today {} {}:'.format(datetime.today().day, datetime.today().strftime('%b')))
        query_result = session.query(Table).filter(Table.deadline == datetime.today().date()).all()
        if not query_result:
            print('Nothing to do!')
        else:
            for items in query_result:
                print('{}. {}'.format(items.id, items.task))
    elif choice == 2:
        daydict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday',
                   5: 'Saturday', 6: 'Sunday'}
        today = datetime.today()
        for i in range(0, 7):
            currday = today + timedelta(days=i)
            print('{} {} {}:'.format(daydict[currday.weekday()], currday.day, currday.strftime('%b')))
            query_result = session.query(Table).filter(Table.deadline == currday.date()).all()
            if not query_result:
                print('Nothing to do!')
            else:
                counter = 1
                for items in query_result:
                    print('{}. {}'.format(counter, items.task))
                    counter += 1
            print()
    elif choice == 3:
        query_result = session.query(Table).order_by(Table.deadline).all()
        print('All tasks:')
        if not query_result:
            print('Nothing to do!')
        else:
            counter = 1
            for items in query_result:
                print('{}. {}. {} {}'.format(counter, items.task, items.deadline.day, items.deadline.strftime('%b')))
                counter += 1
    elif choice == 4:
        query_result = session.query(Table).filter(Table.deadline < datetime.today().date()).order_by(
            Table.deadline).all()
        if not query_result:
            print('Nothing is missed!')
        else:
            counter = 1
            for items in query_result:
                print('{}. {}. {} {}'.format(counter, items.task, items.deadline.day, items.deadline.strftime('%b')))
                counter += 1
    elif choice == 5:
        print('Enter task')
        t = input()
        print('Enter deadline')
        d = input()
        new_row = Table(task=t, deadline=datetime.strptime(d, '%Y-%m-%d').date())
        session.add(new_row)
        session.commit()
        print('The task has been added!')
    elif choice == 6:
        query_result = session.query(Table).order_by(Table.deadline).all()
        if not query_result:
            print('Nothing to delete')
        else:
            print('Choose the number of the task you want to delete:')
            counter = 1
            for items in query_result:
                print('{}. {}. {} {}'.format(counter, items.task, items.deadline.day, items.deadline.strftime('%b')))
                counter += 1
            delidx = int(input())
            session.delete(query_result[delidx-1])
            session.commit()
            print('The task has been deleted!')
    else:
        print('Bye')
        exit(0)

# print('Today:')
# print('1) Do yoga')
# print('2) Make breakfast')
# print('3) Learn basics of SQL')
# print('4) Learn what is ORM')
