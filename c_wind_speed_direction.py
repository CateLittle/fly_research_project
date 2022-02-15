## import json
import matplotlib.pyplot as plt
import numpy as np
import pdb
import pandas as pd
import time
import datetime

##### wind speed-time plot with wind direction #####

wind_data=input("Enter wind data text file you would like to make a plot (e.g. 2021_10_19): ")
release=input("what time did you release flies (e.g. 1420): ")

directory="/mnt/c/Users/Owner/Desktop/field_data_and_analysis_scripts/2021lab/wind_plot/wind_"+wind_data+".txt"
wind_df=pd.read_csv(directory,delimiter=' ',header=None)
wind_df.columns=("time","direction","wind_speed")

released_time=release[0:2]+':'+release[2:4]+':'+'00'
release_sec=int(release[0:2])*3600+int(release[2:4])*60

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

temp_wind_df=[]
temp_wind_df=wind_df.loc[(wind_df['sec_since_release']>=0) & (wind_df['sec_since_release']<=1500)].reset_index(drop=True)
temp_wind_df.head()

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

new_t_list=new_wind_df['sec_since_release']
new_s_list=new_wind_df['wind_speed']
new_d_list=new_wind_df['direction'] 
new_n_list=list(np.arange(1,len(new_t_list)+1))

fig=plt.figure(figsize=(20,10))
ax=plt.axes()
plt.plot(new_n_list, new_s_list, '-',markersize=6,color="r")
plt.xlabel('Time since release (Sec)')
plt.ylabel('Wind Speed')

ax.set_xticks(new_n_list)
ax.set_xticklabels(new_t_list,rotation=45)

x_min=np.min(new_n_list)
x_max=np.max(new_n_list)
y_min=np.min(new_s_list)
y_max=np.max(new_s_list)
ratio=(x_max-x_min)/(y_max-y_min) # to adjust arrow length
for i in range(len(new_n_list)):
    dx=(np.cos(new_d_list[i]))
    dy=(np.sin(new_d_list[i]))
    ax.annotate("",xy=(new_n_list[i],new_s_list[i]),
               xytext=(new_n_list[i]+dx,
                       new_s_list[i]+3*(dy/ratio)),arrowprops=dict(arrowstyle='-'))
    if new_t_list[i]==release:
        ax.axvline(x=i+1,ymax=y_max,ls='--',color='b')

plt.savefig("/mnt/c/Users/Owner/Desktop/field_data_and_analysis_scripts/2021lab/wind_"+wind_data+".png",dpi=600)


