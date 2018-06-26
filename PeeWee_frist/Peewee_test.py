from peewee import *
db = SqliteDatabase('test.db')
class BaseModel(Model):
    class Meta:
        database = db
class Course(BaseModel):
    id = PrimaryKeyField()
    title = CharField(null=False)
    peroid = IntegerField()
    description = CharField()
    class Meta:
        order_by = ('title',)
        da_table = 'course'

class Teacher(BaseModel):
    id = PrimaryKeyField()
    name = CharField(null=False)
    gender = BooleanField()
    address = CharField()
    course_id = ForeignKeyField(Course,to_field='id',related_name='couser')
    class Metra:
        order_by =('name')
        db_table = 'title'

Course.create_table()
Teacher.create_table()

Course.create(id=1,title ='经济学',peroid=320,description='文理科均可以选修')
Course.create(id=2,title ='大学英语',peroid=300,description='大一必修课')
Course.create(id=3,title ='哲学',peroid=100,description='必修课')
Course.create(id=4,title ='编译原理',peroid=100,description='计算机可以选修')

Teacher.create(name='白振军',gender=True,address='',course_id=1)
Teacher.create(name='李僧',gender=True,address='',course_id=3)
Teacher.create(name='张雯雯',gender=False,address='',course_id=2)

record = Course.get(Course.title=='大学英语')
print('课程:%s,学时:%d'%(record.title,record.peroid))

record.peroid =200
record.save()

couses = Course.select()
print('带条件查询')
couses = Course.select().where(Course.id <10).order_by(Course.peroid.desc())
total = Course.select(fn.Avg (Course.peroid).alias('avg_period'))
Course.update(peroid = 300).where(Course.id > 100).execute()
Record = Course.select().join(Teacher).where(Teacher.gender==True)

























