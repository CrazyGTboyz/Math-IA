import csv
import random
import time
import math

x_pos_w = 0
y_pos_w = 0
x_pos_wo = 0
y_pos_wo = 0
grav = 9.81

fieldnames = ['x_pos', 'y_pos']

with open('w_drag_data.csv', 'w') as csv_file_w:
    csv_writer_w = csv.DictWriter(csv_file_w, fieldnames=fieldnames)
    csv_writer_w.writeheader()

with open('wo_drag_data.csv', 'w') as csv_file_wo:
    csv_writer_wo = csv.DictWriter(csv_file_wo, fieldnames=fieldnames)
    csv_writer_wo.writeheader()

while True:

   with open('w_drag_data.csv', 'a') as csv_file_w:
       csv_writer_w = csv.DictWriter(csv_file_w, fieldnames=fieldnames)

       info = {
           "x_pos": x_pos_w,
           "y_pos": y_pos_w
       }

       csv_writer_w.writerow(info)
       print(x_pos_w, y_pos_w)

       x_pos_w += 1
       y_pos_w += random.randint(-5, 5)

   with open('wo_drag_data.csv', 'a') as csv_file_wo:
       csv_writer_wo = csv.DictWriter(csv_file_wo, fieldnames=fieldnames)

       info = {
           "x_pos": x_pos_wo,
           "y_pos": y_pos_wo
       }

       csv_writer_wo.writerow(info)
       print(x_pos_wo, y_pos_wo)

       x_pos_wo += 1
       y_pos_wo = ((-1*grav)/(2*pow(20, 2)))*pow(x_pos_wo, 2) + (10/20)*x_pos_wo + 0

   time.sleep(1)