from pymongo import MongoClient
import uuid
import datetime

def connectcloud(address,port,database,user,password,collection_id):
    connection = MongoClient(address,port)
    db = connection[database]
    db.authenticate(user, password)
    collection = db[collection_id]
    return collection


def initializedata(collection):
    data_dict = [{'Doctor_name':'Changshuo.Hu',
                 'Doctor_specialization':'General Dentist',
                 'Doctor_location':'UNSW Dental Clinic',
                 'Doctor_room':'02 9313 6228',
                 'Doctor_Uni':'Ground Floor, Quadrangle Building'
                 },
                 {'Doctor_name':'Keyang.Li',
                 'Doctor_specialization':'Endodontics',
                 'Doctor_location':'BUPA Dental Kensington',
                 'Doctor_room':'02 9663 1605',
                 'Doctor_Uni':'115 Doncaster Ave'
                 },
                 {'Doctor_name':'Lingxu.Meng',
                 'Doctor_specialization':'Oral medicine',
                 'Doctor_location':'White Smile Dental',
                 'Doctor_room':'02 9663 2062',
                 'Doctor_Uni':'92 Anzac Pde'
                 },
                 {'Doctor_name':'Jiachen.Li',
                 'Doctor_specialization':'Periodontics',
                 'Doctor_location':'D-zire Dental',
                 'Doctor_room':'02 9697 3751',
                 'Doctor_Uni':'Unit 1 3 Defries Ave'
                 }
                 ]
    collectiondata = collection.find()
    for item in collectiondata:
        collection.delete_one({'_id':item['_id']})
    for item in data_dict:
        item['_id'] = str(uuid.uuid4())
        collection.insert_one(item)
    print('initialize dentist data successfully')



def initializetimeslot(collection):
    collection_Doctor = connectcloud('ds161517.mlab.com',61517,'chatbot','huchangshuo','z5187447','DentalClinicDoctor')
    collectionDoctordata = collection_Doctor.find()
    collectiondata  = collection.find()
    for item in collectiondata:
        collection.delete_one({'_id':item['_id']})
    for item in collectionDoctordata:
        for i in range(1,4):
            insert_Day = (datetime.date.today() + datetime.timedelta(days=+i)).strftime('%Y-%m-%d')
            for j in range(9,17):
                dict = {}
                dict['Doctor_name'] = item['Doctor_name']
                dict['Doctor_id'] = item['_id']
                dict['_id']=str(uuid.uuid4())
                dict['Date'] = insert_Day
                if j >= 12:
                    dict['Time'] = str(j) + ':00PM-' + str(j + 1) + ':00PM'
                elif j == 11:
                    dict['Time'] = str(j) + ':00AM-' + str(j + 1) + ':00PM'
                else:
                    dict['Time'] = str(j) + ':00AM-' + str(j + 1) + ':00AM'
                dict['Status'] = 'N'
                dict['Patient_name'] = ''
                collection.insert_one(dict)
    print('initialize timeslot data successfully')

if __name__ == '__main__':
    initializedata(connectcloud('ds161517.mlab.com',61517,'chatbot','huchangshuo','z5187447','DentalClinicDoctor'))
    initializetimeslot(connectcloud('ds161517.mlab.com',61517,'chatbot','huchangshuo','z5187447','DentalClinicTimetable'))