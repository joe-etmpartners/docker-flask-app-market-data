# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:49:04 2022

@author: josep
"""
#import logging

import boto3
#from botocore.exceptions import ClientError
#import os


class S3Skywalker():
    
    def __init__(self):
        pass
    
    def upload_file(self, localFname, targetKey, loader):
        s3_resource = boto3.resource('s3')
        
        # for bucket in s3_resource.buckets.all():
        #     print(bucket.name)
            
        data = open(localFname, 'rb')
        
        #print ('localFname = ' + localFname)
        #print ('targetKey = ' + targetKey)
        #print ('loader = ' + loader)
        
        try: 
            s3_resource.Bucket('s3-skywalker').put_object(Key=targetKey, Body=data)
        except:
            return(0)
        
        return(1)
    
    def upload_content(self, targetKey, loader, content):
        s3_resource = boto3.resource('s3')
        
        # for bucket in s3_resource.buckets.all():
        #     print(bucket.name)
            
        try: 
            s3_resource.Bucket('s3-skywalker').put_object(Key=targetKey, Body=content)
        except:
            return(False)
        
        return(True)
        

if __name__ == '__main__':
    print('This is the S3Skywalker class')
    print('It is not intended to be run directly.')
    print('It is intended to be imported into other modules.')
    print('For example:')
    print('from S3Skywalker import S3Skywalker')
    print('s3skywalker = S3Skywalker()')
    print('s3skywalker.upload_file(localFname, targetKey, loader)')
    print('where:')
    print('localFname is the local file name')
    print('targetKey is the S3 key')
    print('loader is the name of the loader')

    print('\n\nTest upload of requirements.txt to S3')
    s3obj = S3Skywalker()
    s3obj.upload_file('requirements.txt', 'requirements.txt', 'S3SkywalkerTest')
    s3obj.upload_content('contenttest.txt', 'S3SkywalkerTest', 'This is a test of the upload_content method')


