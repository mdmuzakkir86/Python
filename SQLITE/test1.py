import sqlite3

# def create_table():
#     connection = sqlite3.connect('test.db')
#     print("Connected successfully")

#     connection.execute('''CREATE TABLE IF NOT EXISTS insert_tblMedical
#              (assigned_to TEXT NOT NULL)''')
#     print("Table created successfully")

#     connection.close()

# create_table()



inputs = [
    {
      "input": "10905813.jpeg",
      "predicted_boxes": [
        {
          "id": "0dd25d61-30ef-11ec-8ee6-a5a4c16b0fac",
          "label": "Supplier_Terms",
          "xmin": 756,
          "ymin": 497,
          "xmax": 910,
          "ymax": 517,
          "score": 0.9834479,
          "ocr_text": "ZANESVILLE,",
          "status": "correctly_predicted"
        },
        {
          "id": "2d5b7c10-30ef-11ec-8ee6-a5a4c16b0fac",
          "label": "",
          "xmin": 466,
          "ymin": 949,
          "xmax": 1617,
          "ymax": 1062,
          "score": 0,
          "ocr_text": "",
          "status": "",
          "type": "table",
          "cells": [
            {
              "id": "32a90f22-30ef-11ec-8ee6-a5a4c16b0fac",
              "row": 1,
              "col": 2,
              "row_span": 1,
              "col_span": 1,
              "label": "",
              "xmin": 640,
              "ymin": 1009,
              "xmax": 803,
              "ymax": 1030,
              "score": 100,
              "text": "text",
              "status": "",
              "row_label": ""
            },
            {
              "id": "32a90f23-30ef-11ec-8ee6-a5a4c16b0fac",
              "row": 1,
              "col": 1,
              "row_span": 1,
              "col_span": 1,
              "label": "header",
              "xmin": 1043,
              "ymin": 1012,
              "xmax": 1561,
              "ymax": 1029,
              "score": 100,
              "text": "text",
              "status": "",
              "row_label": ""
            }
          ]
        },
        {
          "id": "0dd25d59-30ef-11ec-8ee6-a5a4c16b0fac",
          "label": "invoice_number",
          "xmin": 402,
          "ymin": 256,
          "xmax": 466,
          "ymax": 273,
          "score": 0.70190364,
          "ocr_text": "15238",
          "status": "correctly_predicted"
        }
      ],
      "custom_response": '',
      "assigned_member": "md.muzakkir@gmail.com",
      "page": 0,
      "day_since_epoch": 18919,
      "hour_of_day": 15,
      "request_file_id": "d9fbc6d5-61d2-4c5a-8787-113a4069d5dc",
      "filepath": "uploadedfiles/a5665dfd-3619-4d35-8fec-694db39c5a77/PredictionImages/1376246724.jpeg",
      "id": "94d8be28-30ee-11ec-9956-0242ac120004",
      "is_moderated": "False",
      "rotation": 0,
      "updated_at": "331196ba-30ef-11ec-99fa-0242ac120004"
    }
  ]


def insert_tblMedical(assigned_member):
    connection = sqlite3.connect('test.db')
    print("Connected successfully")

    columns = '(assigned_to)'
    values = ("('"+assigned_member+"')")
    
    query = "insert into insert_tblMedical " + columns + " values " + values
    connection.execute(query)
    print("assigned_to=", assigned_member)

    connection.commit()
    print('Record inserted successfully')
    connection.close()



def handler(inputs):
    
    for page in inputs:
        assigned_member = page.get("assigned_member")
        insert_tblMedical(assigned_member)     
    print(type(inputs))
    return inputs

handler(inputs)









