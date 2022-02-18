from math import radians
import matplotlib.pyplot as plt
import numpy as np
import pdb
import time
import datetime
import sys
import json
import pandas as pd

wind_data=input("Enter wind data text file you would like to make a plot (e.g. 2021_10_19): ")

directory="/home/flyranch/field_data_and_analysis_scripts/2021lab/wind_data_files/wind_"+wind_data+".txt"
#directory="wind_"+wind_data+".txt"
wind_df=pd.read_csv(directory,delimiter=' ',header=None)
wind_df.columns=("time","direction","wind_speed")

released_time=release[0:2]+':'+release[2:4]+':'+'00'
release_sec=int(release[0:2])*3600+int(release[2:4])*60
release_sec

time_list=[]
sec_since_release_list=[]
min_since_release_list=[]

for i in wind_df.iloc[:,0]:
    time=datetime.datetime.fromtimestamp(i)
    str_h=str(time.hour)
    str_m=str(time.minute)
    str_s=str(time.second)
    if len(str_h)==1:
        str_h='0'+str_h
    if len(str_m)==1:
        str_m='0'+str_m
    if len(str_s)==1:
        str_s='0'+str_s
    #str_time=int(str_h)*3600+int(str_m)*60+int(str_s)-release_sec
    str_time=int(str_h)*3600+int(str_m)*60-release_sec
    str_min=int(str_time)/60
    sec_since_release_list.append(str_time)
    min_since_release_list.append(str_min)
    
wind_df['sec_since_release']=sec_since_release_list
wind_df['min_since_release']=min_since_release_list

rad_d_list=[]
mean_angle_list=[]

### in minutes
temp_wind_df=[]
temp_wind_df=wind_df.loc[(wind_df['min_since_release']>=-5) & (wind_df['min_since_release']<=25)].reset_index(drop=True)

for i in range(len(temp_wind_df)): 
    math_d=270-temp_wind_df['direction'][i] # need to convert from weather direction to math angle
    if math_d<0:
        math_d=math_d+360
    rad=np.deg2rad(math_d) # convert to degree to radian
    if i==0:
        rad_d_list.append(rad)
        #mean_angle=np.arctan2(np.nanmean(np.sin(rad_d_list)),np.nanmean(np.cos(rad_d_list)))
        #mean_angle_list.append(mean_angle)
    if (i!=0) and (temp_wind_df['min_since_release'][i]==temp_wind_df['min_since_release'][i-1]):
        if i==(len(temp_wind_df)-1):
            rad_d_list.append(rad)
            mean_angle=np.arctan2(np.nanmean(np.sin(rad_d_list)),np.nanmean(np.cos(rad_d_list)))    
            mean_angle_list.append(mean_angle)
        else:
            rad_d_list.append(rad)
    if (i!=0) and (temp_wind_df['min_since_release'][i]!=temp_wind_df['min_since_release'][i-1]):
        if i==(len(temp_wind_df)-1):
            rad_d_list.append(rad)
            mean_angle=np.arctan2(np.nanmean(np.sin(rad_d_list)),np.nanmean(np.cos(rad_d_list)))    
            mean_angle_list.append(mean_angle)
        else:       
            mean_angle=np.arctan2(np.nanmean(np.sin(rad_d_list)),np.nanmean(np.cos(rad_d_list)))    
            mean_angle_list.append(mean_angle)
            rad_d_list=[]
            rad_d_list.append(rad)

new_wind_df=temp_wind_df.groupby(['min_since_release'], as_index=False).mean()
new_wind_df['direction']=mean_angle_list

new_t_m_list=new_wind_df['min_since_release']
new_s_list=new_wind_df['wind_speed']
new_d_list=new_wind_df['direction'] 
new_n_m_list=list(np.arange(1,len(new_t_m_list)+1))

import numpy as np
from scipy.stats import binned_statistic

bin_t_m_means = binned_statistic(new_t_m_list, new_t_m_list, statistic='mean',bins=6)[1]
bin_s_means = binned_statistic(new_s_list, new_s_list, statistic='mean',bins=6)[1]
bin_d_means = binned_statistic(new_d_list, new_d_list, statistic='mean',bins=6)[1]
bin_n_m_means = binned_statistic(new_n_m_list, new_n_m_list, statistic='mean',bins=6)[1]

bin_df = pd.DataFrame(list(zip(bin_t_m_means, bin_s_means, bin_d_means, bin_n_m_means)),
               columns =['t_m_means', 's_means', 'd_means', 'n_m_means'])

fig=plt.figure(figsize=(30,20))
line=np.ones(7)
plt.xlabel('Time since release (Min)')
plt.ylabel('Wind Speed')

rad_dir_list=np.deg2rad(90-np.rad2deg(bin_d_means))

I=15.0 # degree for trap I
J=195.0 # degree for trap J

theta1=np.deg2rad([I,I]) # trap I
theta2=np.deg2rad([J,J]) # trap J
r=[0,2.0]

min_len=7 # from 5 min before release to 25 min after release
a=1 #number of rows
b=7 #number of columns
c=1 #plot counter
release_time=0

for i in np.arange(min_len):
    ax3=plt.axes()
    ax3=plt.subplot(a,b,c, polar=True)
    ax3.set_ylim(0,2)
    ax3.set_yticks(np.arange(0,2,2)) 
    ax3.set_theta_zero_location('N')
    ax3.set_theta_direction('clockwise')
    ax3.xaxis.set_label_position('bottom')
    ax3.set_xlabel(str(bin_t_m_means[i])+' minutes since release'+'\n'+str(round(bin_s_means[i],3))+ ' m/s')
    if i == 0:
        ax3.plot(theta1,r,'r')
        ax3.plot(theta2,r,'b')
        ax3.text(np.radians(I),ax3.get_rmax()+0.2,'trap I (15°)',
            ha='center',va='center')
        ax3.text(np.radians(J),ax3.get_rmax()+0.2,'trap J (195°)',
            ha='center',va='center')
        #ax3.text(np.radians(0),ax3.get_rmax()+0.5, str(bin_t_m_means[i])+'minutes since release'+'\n'+str(round(bin_s_means[i],3))+ 'm/s',
        #    ha='center',va='top')
        wind_d_theta=[rad_dir_list[i],rad_dir_list[i]]
        ax3.plot(wind_d_theta,[0,bin_s_means[i]],marker='X',ls='--',color='k')
        c=c+1
    else:
        #ax3.text(np.radians(0),ax3.get_rmax()+0.5,str(bin_t_m_means[i])+'minutes since release'+'\n'+str(round(bin_s_means[i],3))+ 'm/s',
        #    ha='center',va='top')
        wind_d_theta=[rad_dir_list[i],rad_dir_list[i]]
        ax3.plot(wind_d_theta,[0,bin_s_means[i]],marker='X',ls='--',color='k')
        c=c+1

plt.text(0.7, 3,'c_wind_plotting.py')
#path="/home/flyranch/field_data_and_analysis_scripts/2021lab/wind_plot/"
path='/Users/Owner/Desktop/field_data_and_analysis_scripts/2021lab/wind_plot/'
plt.savefig(path+'wind_circular_plots_'+wind_data+'.png')
