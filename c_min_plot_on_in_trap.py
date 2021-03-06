import json
import matplotlib
import matplotlib.pyplot as plt
import time
import pandas as pd
import numpy as np
import pdb
import sys
import datetime as dt
import matplotlib.dates as md
#modified TW to save EPS

#ask user input
#trap=input("Enter a trap letter to analyze (e.g. yyyy_mm_dd_A): ")
file_prefix='/Users/tim/BoxSync/Warren-Lab/all_traps_final_analysis_json_files/'



f_I=open(file_prefix+ 'trap_2021_10_30_I/master_trap_2021_10_30_I.json')
f_J=open(file_prefix+ 'trap_2021_10_30_J/master_trap_2021_10_30_J.json')

#f=open('/mnt/c/Users/Owner/Desktop/field_data_and_analysis_scripts/2021lab/all_traps_final_analysis_json_files/trap_'+trap+'/master_trap_'+trap+'.json')
data_I=json.load(f_I)
data_J=json.load(f_J)


release='142000'
released_time=release[0:2]+':'+release[2:4]+':'+release[4:6]

released_time=release[0:2]+':'+release[2:4]+':'+release[4:6]

#create lists



def calc_sec_since_release(standard,time_stamp):
	zero=int(standard[0:2])*3600+int(standard[3:5])*60+int(standard[6:8])+1
	sec=int(time_stamp[0:2])*3600+int(time_stamp[3:5])*60+int(time_stamp[6:8])
	sec_since_release=sec-zero
	return sec_since_release

def make_timestamps(indata):
	on_trap_list=[]
	in_trap_list=[]
	sec_since_release_list=[]
	actual_timestamp_list=[]
	min_since_release_list=[]

	ret_dict={}

	for i in indata:
		for k in indata[i]:
			if i=="flies on trap over time:":
				on_trap_list.append(k)
			elif i=="flies in trap over time:":
				in_trap_list.append(k)
			elif i=="actual timestamp:":
				if len(str(int(k)))==5:
					str_time='0'+str(int(k))[0:1]+':'+str(int(k))[1:3]+':'+str(int(k))[3:5]
					actual_timestamp_list.append(str_time)
				elif len(str(int(k)))==6:
					str_time=str(int(k))[0:2]+':'+str(int(k))[2:4]+':'+str(int(k))[4:6]
					actual_timestamp_list.append(str_time)


	for i in actual_timestamp_list:
		s=calc_sec_since_release(released_time,i)
		if s>=-302:
			sec_since_release_list.append(s)

	ret_dict['on_trap_list']=on_trap_list
	ret_dict['in_trap_list']=in_trap_list
	ret_dict['sec_since_release_list']=sec_since_release_list
	return ret_dict


rd_I=make_timestamps(data_I['trap_2021_10_30_I'])
rd_J=make_timestamps(data_J['trap_2021_10_30_J'])

interp_xvls=np.linspace(-5,25,450)
on_trapI=np.interp(interp_xvls,np.array(rd_I['sec_since_release_list'][:1500])/60,rd_I['on_trap_list'][:1500])
in_trapI=np.interp(interp_xvls,np.array(rd_I['sec_since_release_list'][:1500])/60,rd_I['in_trap_list'][:1500])
on_trapJ=np.interp(interp_xvls,np.array(rd_J['sec_since_release_list'][:1500])/60,rd_J['on_trap_list'][:1500])


f_I.close()
f_J.close()




#to plot 5 min before release
#pdb.set_trace()


# remove first 4min
#on_trap_list=on_trap_list[120:]

#min_since_release_list=[sec / 60 for sec in sec_since_release_list]
#t = pd.to_datetime(min_since_release_list, unit='m') # convert to datetime

# to name output file
ind=0

fig=plt.figure()
#axm=plt.axes()
axm = fig.add_subplot(211)
#fig.autofmt_xdate() # auto format

#xformatter = md.DateFormatter('%M:%S')
#xlocator = md.MinuteLocator(interval = 5)
#formatter = matplotlib.ticker.FuncFormatter(lambda ms, x: time.strftime('%M:%S', time.gmtime(ms // 1000)))
#ax.xaxis.set_major_locator(xlocator)
#ax.xaxis.set_major_formatter(xformatter)
#plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
# to set range xlim, ylim
#plt.xlim(-300,1500)
#plt.ylim(-0.5,75)

#axm.set_xlabel('Time since release (min)')
#axm.set_ylabel('Flies at trap')
axm.plot(interp_xvls,on_trapI)
axm.plot(interp_xvls,in_trapI)
axm.set_aspect(0.3)
axm.set_xticks([-5,0,5,10,15,20,25])

#set dark back ground
#axm.patch.set_facecolor('white')
#fig.patch.set_facecolor('white')

# set thick param and label color
#axm.tick_params(axis='x', colors='black')
#axm.tick_params(axis='y', colors='black')
#axm.yaxis.label.set_color('black')
#axm.xaxis.label.set_color('black')
#axm.set_xticks([-300,0,300,600,900,1200,1500])
#axm.set_xticklabels([-5,0,5,10,15,20,25])

# hide spines
axm.spines['top'].set_visible(False)
axm.spines['right'].set_visible(False)

axm.spines['left'].set_color('black')
axm.spines['bottom'].set_color('black') 


axm = fig.add_subplot(212)
axm.plot(interp_xvls,on_trapI)
axm.plot(interp_xvls,on_trapJ)
axm.set_aspect(0.3)
axm.set_xticks([-5,0,5,10,15,20,25])
#axm.set_xticklabels([-5,0,5,10])

#in advance, plot data till 1500 sec
#axm.plot(sec_since_release_list[:1500], on_trap_list[:1500], '-',markersize=4,color="r",label="on trap")
#plt.savefig('/mnt/c/Users/Owner/Desktop/field_data_and_analysis_scripts/2021lab/plots_for_2021_10_30_traps/plots_for_'+trap+'/trap_'+trap+'_'+str(0)+'.svg')
#pdb.set_trace()

# 360 sec to 760 sec
#for i in range(len(sec_since_release_list[:282])):
	#on_trap_plt=ax.plot(sec_since_release_list[55:i], on_trap_list[55:i], '-',markersize=6,color="r",label="on trap")
	#on_trap_plt=ax.plot(sec_since_release_list[55:i], on_trap_list[55:i], '-',markersize=6,color="r")
	#plt.savefig('/mnt/c/Users/Owner/Desktop/field_data_and_analysis_scripts/2021lab/plots_for_2021_10_30_traps/plots_for_'+trap+'/trap_'+trap+'_'+str(ind)+'.svg')
	#ind+=1


#plt.savefig('/mnt/c/Users/Owner/Desktop/field_data_and_analysis_scripts/2021lab/plots_for_2021_10_30_traps/plots_for_'+trap+'/trap_'+trap+'_'+str(ind)+'.svg',dpi=600)

# remove first 4min
#in_trap_list=in_trap_list[120:]

#in_trap_plt=axm.plot(sec_since_release_list[:1500], in_trap_list[:1500], '-',markersize=4,color="b",label="in trap")
#plt.legend(loc='upper left')
#plt.text(1100, 75,'c_min_plot_on_in_trap.py')

#plt.savefig('/mnt/c/Users/Owner/Desktop/field_data_and_analysis_scripts/2021lab/plots_for_2021_10_30_traps/plots_for_'+trap+'/trap_'+trap+'_'+'min'+'.png',dpi=600)


plt.savefig(file_prefix+'compare_2m_traps.pdf',dpi=600,transparent=True)


