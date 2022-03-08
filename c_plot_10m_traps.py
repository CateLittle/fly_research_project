import matplotlib.pyplot as plt
import numpy as np
import pdb
import time
import datetime
import sys
import json
from matplotlib.pyplot import figure
import matplotlib as mpl
mpl.rcParams['pdf.fonttype']=42
mpl.rcParams['ps.fonttype'] = 42




#6 traps
trap_A='2021_10_30_A'
trap_B='2021_10_30_B'
trap_D='2021_10_30_D'
trap_E='2021_10_30_E'
trap_F='2021_10_30_F'
trap_G='2021_10_30_G'

file_prefix='/Users/tim/BoxSync/Warren-Lab/all_traps_final_analysis_json_files/'

#f_A=open('/home/flyranch/field_data_and_analysis_scripts/2021lab/all_traps_final_analysis_json_files/trap_2021_10_30_A/master_trap_2021_10_30_A.json')
f_A=open(file_prefix +'trap_2021_10_30_A/master_trap_2021_10_30_A.json')
data_A=json.load(f_A)
#f_B=open('/home/flyranch/field_data_and_analysis_scripts/2021lab/all_traps_final_analysis_json_files/trap_2021_10_30_B/master_trap_2021_10_30_B.json')
f_B=open(file_prefix+'trap_2021_10_30_B/master_trap_2021_10_30_B.json')
data_B=json.load(f_B)
#f_I=open('/home/flyranch/field_data_and_analysis_scripts/2021lab/all_traps_final_analysis_json_files/trap_2021_10_30_D/master_trap_2021_10_30_D.json')
f_D=open(file_prefix+'trap_2021_10_30_D/master_trap_2021_10_30_D.json')
data_D=json.load(f_D)
#f_F=open('/home/flyranch/field_data_and_analysis_scripts/2021lab/all_traps_final_analysis_json_files/trap_2021_10_30_E/master_trap_2021_10_30_E.json')
f_E=open(file_prefix+'trap_2021_10_30_E/master_trap_2021_10_30_E.json')
data_E=json.load(f_E)
#f_F=open('/home/flyranch/field_data_and_analysis_scripts/2021lab/all_traps_final_analysis_json_files/trap_2021_10_30_F/master_trap_2021_10_30_F.json')
f_F=open(file_prefix+'trap_2021_10_30_F/master_trap_2021_10_30_F.json')
data_F=json.load(f_F)
#f_G=open('/home/flyranch/field_data_and_analysis_scripts/2021lab/all_traps_final_analysis_json_files/trap_2021_10_30_G/master_trap_2021_10_30_G.json')
f_G=open(file_prefix+'trap_2021_10_30_G/master_trap_2021_10_30_G.json')
data_G=json.load(f_G)

release='142000'
released_time=release[0:2]+':'+release[2:4]+':'+release[4:6]

#create lists
on_trap_list_A=[]
on_trap_list_B=[]
on_trap_list_D=[]
on_trap_list_E=[]
on_trap_list_F=[]
on_trap_list_G=[]

sec_since_release_list_A=[]
actual_timestamp_list_A=[]
sec_since_release_list_B=[]
actual_timestamp_list_B=[]
sec_since_release_list_D=[]
actual_timestamp_list_D=[]
sec_since_release_list_E=[]
actual_timestamp_list_E=[]
sec_since_release_list_F=[]
actual_timestamp_list_F=[]
sec_since_release_list_G=[]
actual_timestamp_list_G=[]


for i in data_A['trap_'+trap_A]:
    for k in data_A['trap_'+trap_A][i]:
        if i=="flies on trap over time:":
            on_trap_list_A.append(k)
        elif i=="actual timestamp:":
            if len(str(int(k)))==5:
                str_time='0'+str(int(k))[0:1]+':'+str(int(k))[1:3]+':'+str(int(k))[3:5]
                actual_timestamp_list_A.append(str_time)
            elif len(str(int(k)))==6:
                str_time=str(int(k))[0:2]+':'+str(int(k))[2:4]+':'+str(int(k))[4:6]
                actual_timestamp_list_A.append(str_time)

f_A.close()

for i in data_B['trap_'+trap_B]:
    for k in data_B['trap_'+trap_B][i]:
        if i=="flies on trap over time:":
            on_trap_list_B.append(k)
        elif i=="actual timestamp:":
            if len(str(int(k)))==5:
                str_time='0'+str(int(k))[0:1]+':'+str(int(k))[1:3]+':'+str(int(k))[3:5]
                actual_timestamp_list_B.append(str_time)
            elif len(str(int(k)))==6:
                str_time=str(int(k))[0:2]+':'+str(int(k))[2:4]+':'+str(int(k))[4:6]
                actual_timestamp_list_B.append(str_time)
                        
f_B.close()

for i in data_D['trap_'+trap_D]:
    for k in data_D['trap_'+trap_D][i]:
        if i=="flies on trap over time:":
            on_trap_list_D.append(k)
        elif i=="actual timestamp:":
            if len(str(int(k)))==5:
                str_time='0'+str(int(k))[0:1]+':'+str(int(k))[1:3]+':'+str(int(k))[3:5]
                actual_timestamp_list_D.append(str_time)
            elif len(str(int(k)))==6:
                str_time=str(int(k))[0:2]+':'+str(int(k))[2:4]+':'+str(int(k))[4:6]
                actual_timestamp_list_D.append(str_time)

f_D.close()

for i in data_E['trap_'+trap_E]:
    for k in data_E['trap_'+trap_E][i]:
        if i=="flies on trap over time:":
            on_trap_list_E.append(k)
        elif i=="actual timestamp:":
            if len(str(int(k)))==5:
                str_time='0'+str(int(k))[0:1]+':'+str(int(k))[1:3]+':'+str(int(k))[3:5]
                actual_timestamp_list_E.append(str_time)
            elif len(str(int(k)))==6:
                str_time=str(int(k))[0:2]+':'+str(int(k))[2:4]+':'+str(int(k))[4:6]
                actual_timestamp_list_E.append(str_time)
                        
f_E.close()


for i in data_F['trap_'+trap_F]:
    for k in data_F['trap_'+trap_F][i]:
        if i=="flies on trap over time:":
            on_trap_list_F.append(k)
        elif i=="actual timestamp:":
            if len(str(int(k)))==5:
                str_time='0'+str(int(k))[0:1]+':'+str(int(k))[1:3]+':'+str(int(k))[3:5]
                actual_timestamp_list_F.append(str_time)
            elif len(str(int(k)))==6:
                str_time=str(int(k))[0:2]+':'+str(int(k))[2:4]+':'+str(int(k))[4:6]
                actual_timestamp_list_F.append(str_time)

f_F.close()

for i in data_G['trap_'+trap_G]:
    for k in data_G['trap_'+trap_G][i]:
        if i=="flies on trap over time:":
            on_trap_list_G.append(k)
        elif i=="actual timestamp:":
            if len(str(int(k)))==5:
                str_time='0'+str(int(k))[0:1]+':'+str(int(k))[1:3]+':'+str(int(k))[3:5]
                actual_timestamp_list_G.append(str_time)
            elif len(str(int(k)))==6:
                str_time=str(int(k))[0:2]+':'+str(int(k))[2:4]+':'+str(int(k))[4:6]
                actual_timestamp_list_G.append(str_time)
                        
f_G.close()

def calc_sec_since_release_A(standard,time_stamp):
    zero=int(standard[0:2])*3600+int(standard[3:5])*60+int(standard[6:8])+1
    sec_A=int(time_stamp[0:2])*3600+int(time_stamp[3:5])*60+int(time_stamp[6:8])
    sec_since_release_A=sec_A-zero
    return sec_since_release_A

def calc_sec_since_release_B(standard,time_stamp):
    zero=int(standard[0:2])*3600+int(standard[3:5])*60+int(standard[6:8])+1
    sec_B=int(time_stamp[0:2])*3600+int(time_stamp[3:5])*60+int(time_stamp[6:8])
    sec_since_release_B=sec_B-zero
    return sec_since_release_B

def calc_sec_since_release_D(standard,time_stamp):
    zero=int(standard[0:2])*3600+int(standard[3:5])*60+int(standard[6:8])+1
    sec_D=int(time_stamp[0:2])*3600+int(time_stamp[3:5])*60+int(time_stamp[6:8])
    sec_since_release_D=sec_D-zero
    return sec_since_release_D

def calc_sec_since_release_E(standard,time_stamp):
    zero=int(standard[0:2])*3600+int(standard[3:5])*60+int(standard[6:8])+1
    sec_E=int(time_stamp[0:2])*3600+int(time_stamp[3:5])*60+int(time_stamp[6:8])
    sec_since_release_E=sec_E-zero
    return sec_since_release_E

def calc_sec_since_release_F(standard,time_stamp):
    zero=int(standard[0:2])*3600+int(standard[3:5])*60+int(standard[6:8])+1
    sec_F=int(time_stamp[0:2])*3600+int(time_stamp[3:5])*60+int(time_stamp[6:8])
    sec_since_release_F=sec_F-zero
    return sec_since_release_F

def calc_sec_since_release_G(standard,time_stamp):
    zero=int(standard[0:2])*3600+int(standard[3:5])*60+int(standard[6:8])+1
    sec_G=int(time_stamp[0:2])*3600+int(time_stamp[3:5])*60+int(time_stamp[6:8])
    sec_since_release_G=sec_G-zero
    return sec_since_release_G

#to plot 5 min before release
for i in actual_timestamp_list_A:
    s_A=calc_sec_since_release_A(released_time,i)
    if s_A>=-302:
        sec_since_release_list_A.append(s_A)
   
for i in actual_timestamp_list_B:
    s_B=calc_sec_since_release_B(released_time,i)
    if s_B>=-302:
        sec_since_release_list_B.append(s_B)

for i in actual_timestamp_list_D:
    s_D=calc_sec_since_release_D(released_time,i)
    if s_D>=-302:
        sec_since_release_list_D.append(s_D)
   
for i in actual_timestamp_list_E:
    s_E=calc_sec_since_release_E(released_time,i)
    if s_E>=-302:
        sec_since_release_list_E.append(s_E)

for i in actual_timestamp_list_F:
    s_F=calc_sec_since_release_F(released_time,i)
    if s_F>=-302:
        sec_since_release_list_F.append(s_F)
   
for i in actual_timestamp_list_G:
    s_G=calc_sec_since_release_G(released_time,i)
    if s_G>=-302:
        sec_since_release_list_G.append(s_G)

ind=0


interp_xvls=np.linspace(-2,10,360)

a=np.interp(interp_xvls,np.array(sec_since_release_list_A[:1500])/60,on_trap_list_A[:1500])
b=np.interp(interp_xvls,np.array(sec_since_release_list_B[:1500])/60,on_trap_list_B[:1500])
g=np.interp(interp_xvls,np.array(sec_since_release_list_G[:1500])/60,on_trap_list_G[:1500])
e=np.interp(interp_xvls,np.array(sec_since_release_list_E[:1500])/60,on_trap_list_E[:1500])
f=np.interp(interp_xvls,np.array(sec_since_release_list_F[:1500])/60,on_trap_list_F[:1500])
d=np.interp(interp_xvls,np.array(sec_since_release_list_D[:1500])/60,on_trap_list_D[:1500])
fig=plt.figure()
ax1=fig.add_subplot(211)
ax1.plot(d)
ax1.set_ylim([0,15])
ax1.set_xlim([-2,10])
ax1.set_yticks([0,5,10,15])
ax1.set_xticks([0,60,120,180,240,300,360])
ax1.set_xticklabels([-2,0,2,4,6,8,10])

ax=fig.add_subplot(212)
on_trap_array=np.vstack((d,e,f,a,b,g))
#print(np.shape(on_trap_array))
plt.imshow(on_trap_array,cmap='hot',interpolation='nearest',aspect='auto')
plt.colorbar(shrink=0.8,orientation='horizontal')
ax.set_xticks([0,60,120,180,240,300,360])
ax.set_xticklabels([-2,0,2,4,6,8,10])
fig.tight_layout()
plt.savefig(file_prefix+'image.pdf',dpi=600,transparent=True)


fig=plt.figure()
from pylab import rcParams
rcParams['figure.figsize'] = 5, 10
#fig, axs = plt.subplots(6, 1, figsize=(5, 8), constrained_layout=True, sharex=True, sharey=True)
#ax1=plt.axes()
ax1 = fig.add_subplot(111)

plt.xlim(-300,1500)
plt.ylim(-0.5,15)



#ax1.set_title('Flies on 10m traps')

#set dark back ground
ax1.patch.set_facecolor('white')
fig.patch.set_facecolor('white')

fig.tight_layout()

# set thick param and label color
ax1.tick_params(axis='x', colors='black')
ax1.tick_params(axis='y', colors='black')
ax1.yaxis.label.set_color('black')
ax1.xaxis.label.set_color('black')


ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax1.spines['left'].set_color('black')
ax1.spines['bottom'].set_color('black') 



ax1=fig.add_subplot(211)
ax1.plot(sec_since_release_list_A[:1500], on_trap_list_A[:1500], '-',markersize=0.5,color="b",label="Trap A")
ax1.plot(sec_since_release_list_B[:1500], on_trap_list_B[:1500], '-',markersize=0.5,color="r",label="Trap B")
ax1.plot(sec_since_release_list_G[:1500], on_trap_list_G[:1500], '-',markersize=0.5,color="g",label="Trap G")
ax1.spines['bottom'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
#fig.suptitle('Flies on 10m traps', fontsize=16)
#ax1.set_title('Trap A')
plt.xlim(-300,600)
ax1.set_xticks([-300,0,300,600])
ax1.set_xticklabels([-5,0,5,10])
plt.ylim(-0.5,15)
#ax1.set_xticks([])
plt.subplots_adjust(left=0.15)
plt.subplots_adjust(top=0.85)

ax1=fig.add_subplot(212)



ax1.plot(sec_since_release_list_D[:1500], on_trap_list_D[:1500], '-',markersize=0.5,color="c",label="Trap D")
ax1.plot(sec_since_release_list_E[:1500], on_trap_list_E[:1500], '-',markersize=0.5,color="k",label="Trap E")
ax1.plot(sec_since_release_list_F[:1500], on_trap_list_F[:1500], '-',markersize=0.5,color="m",label="Trap F")


#plt.legend(loc='upper right')
ax1.spines['bottom'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
#fig.suptitle('Flies on 10m traps', fontsize=16)
#ax1.set_title('Trap A')
plt.xlim(-300,600)
ax1.set_xticks([-300,0,300,600])
ax1.set_xticklabels([-5,0,5,10])
plt.ylim(-0.5,15)
#ax1.set_xticks([])
#plt.subplots_adjust(left=0.15)
#plt.subplots_adjust(top=0.85)




#plt.text(900, 160,'c_plot_10m_traps.py')

plt.savefig(file_prefix+'compare_10m_traps.pdf',dpi=600,transparent=True)