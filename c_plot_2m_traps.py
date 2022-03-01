import matplotlib.pyplot as plt
import numpy as np
import pdb
import time
import datetime
import sys
import json

#2 traps
trap_I='2021_10_30_I'
trap_J='2021_10_30_J'

#f_I=open('/home/flyranch/field_data_and_analysis_scripts/2021lab/all_traps_final_analysis_json_files/trap_2021_10_30_I/master_trap_2021_10_30_I.json')
f_I=open('/mnt/c/Users/Owner/Desktop/field_data_and_analysis_scripts/2021lab/all_traps_final_analysis_json_files/trap_2021_10_30_I/master_trap_2021_10_30_I.json')
data_I=json.load(f_I)
#f_J=open('/home/flyranch/field_data_and_analysis_scripts/2021lab/all_traps_final_analysis_json_files/trap_2021_10_30_J/master_trap_2021_10_30_J.json')
f_J=open('/mnt/c/Users/Owner/Desktop/field_data_and_analysis_scripts/2021lab/all_traps_final_analysis_json_files/trap_2021_10_30_J/master_trap_2021_10_30_J.json')
data_J=json.load(f_J)

release='142000'
released_time=release[0:2]+':'+release[2:4]+':'+release[4:6]

#create lists
on_trap_list_I=[]
in_trap_list_I=[]
sec_since_release_list_I=[]
actual_timestamp_list_I=[]

on_trap_list_J=[]
in_trap_list_J=[]
sec_since_release_list_J=[]
actual_timestamp_list_J=[]

for i in data_I['trap_'+trap_I]:
    for k in data_I['trap_'+trap_I][i]:
        if i=="flies on trap over time:":
            on_trap_list_I.append(k)
        elif i=="flies in trap over time:":
            in_trap_list_I.append(k)
        elif i=="actual timestamp:":
            if len(str(int(k)))==5:
                str_time='0'+str(int(k))[0:1]+':'+str(int(k))[1:3]+':'+str(int(k))[3:5]
                actual_timestamp_list_I.append(str_time)
            elif len(str(int(k)))==6:
                str_time=str(int(k))[0:2]+':'+str(int(k))[2:4]+':'+str(int(k))[4:6]
                actual_timestamp_list_I.append(str_time)

f_I.close()

for i in data_J['trap_'+trap_J]:
    for k in data_J['trap_'+trap_J][i]:
        if i=="flies on trap over time:":
            on_trap_list_J.append(k)
        elif i=="flies in trap over time:":
            in_trap_list_J.append(k)                
        elif i=="actual timestamp:":
            if len(str(int(k)))==5:
                str_time='0'+str(int(k))[0:1]+':'+str(int(k))[1:3]+':'+str(int(k))[3:5]
                actual_timestamp_list_J.append(str_time)
            elif len(str(int(k)))==6:
                str_time=str(int(k))[0:2]+':'+str(int(k))[2:4]+':'+str(int(k))[4:6]
                actual_timestamp_list_J.append(str_time)
                        
f_J.close()

def calc_sec_since_release_I(standard,time_stamp):
    zero=int(standard[0:2])*3600+int(standard[3:5])*60+int(standard[6:8])+1
    sec_I=int(time_stamp[0:2])*3600+int(time_stamp[3:5])*60+int(time_stamp[6:8])
    sec_since_release_I=sec_I-zero
    return sec_since_release_I


def calc_sec_since_release_J(standard,time_stamp):
    zero=int(standard[0:2])*3600+int(standard[3:5])*60+int(standard[6:8])+1
    sec_J=int(time_stamp[0:2])*3600+int(time_stamp[3:5])*60+int(time_stamp[6:8])
    sec_since_release_J=sec_J-zero
    return sec_since_release_J

release='142000'
released_time=release[0:2]+':'+release[2:4]+':'+release[4:6]

#to plot 5 min before release
for i in actual_timestamp_list_I:
    s_I=calc_sec_since_release_I(released_time,i)
    if s_I>=-302:
        sec_since_release_list_I.append(s_I)

       
for i in actual_timestamp_list_J:
    s_J=calc_sec_since_release_J(released_time,i)
    if s_J>=-302:
        sec_since_release_list_J.append(s_J)

ind=0

fig=plt.figure()
ax1=plt.axes()
ax1 = fig.add_subplot(111)
plt.xlim(-300,1500)
plt.ylim(-0.5,75)

ax1.set_xlabel('Time since release (min)')
ax1.set_ylabel('Flies on trap')
ax1.set_title('Flies on upwind and downwind 2m traps')

#set dark back ground
ax1.patch.set_facecolor('white')
fig.patch.set_facecolor('white')

# set thick param and label color
ax1.tick_params(axis='x', colors='black')
ax1.tick_params(axis='y', colors='black')
ax1.yaxis.label.set_color('black')
ax1.xaxis.label.set_color('black')
ax1.set_xticks([-300,0,300,600,900,1200,1500])
ax1.set_xticklabels([-5,0,5,10,15,20,25])

# hide spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax1.spines['left'].set_color('black')
ax1.spines['bottom'].set_color('black') 

ax1.plot(sec_since_release_list_I[:1500], on_trap_list_I[:1500], '-',markersize=4,color="b",label="Trap I - upwind")
compare_plot=ax1.plot(sec_since_release_list_J[:1500], on_trap_list_J[:1500], '-',markersize=4,color="k",label="Trap J - downwind")
plt.legend(loc='upper left')
plt.text(1100, 65,'c_plot_2m_traps.py')

plt.savefig('/mnt/c/Users/Owner/Desktop/field_data_and_analysis_scripts/2021lab/plots_for_2021_10_30_traps/compare_2m_traps.png',dpi=600)