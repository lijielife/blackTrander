#from ctaBase import *
#from ctaTemplate import CtaTemplate
import os,sys
import json
print "hello world!"

########################################################################
#//class PirateStrategy(CtaTemplate):
class PirateStrategy(object):
    """�������ײ���"""
    settingFileName = 'pirate_setting.json'
    path = os.path.abspath(os.path.dirname(__file__))
    settingFileName = os.path.join(path, settingFileName)      

    maket_situation = 0; #0 �����𵴣�1 ���ƶ࣬2 ���ƿ� 
    strategy_type = 1; #0 
    y_open_price = 1; #yestday opening price
    y_close_price = 2;
    y_highest_price = 1;
    y_lowest_price = 1;
    M20_high = 21;
    M20_low = 123;
    
    
    #----------------------------------------------------------------------
    def __init__(self):
    #def __init__(self, ctaEngine, setting):
        #"""Constructor"""
        #super(EmaDemoStrategy, self).__init__(ctaEngine, setting)
        
        # ע��������еĿɱ�������ԣ�ͨ����list��dict�ȣ����ڲ��Գ�ʼ��ʱ��Ҫ���´�����
        # �������ֶ������ʵ��֮�����ݹ����������п��ܵ���Ǳ�ڵĲ����߼�������գ�
        # �������е���Щ�ɱ�������Կ���ѡ��д��ȫ������__init__���棬д��Ҫ��Ϊ���Ķ�
        # ����ʱ���㣨�����Ǹ����ϰ�ߵ�ѡ��
        self.fastMa = []
        self.slowMa = []    
    #----------------------------------------------------------------------
    def loadStrategySetting(self):
        with open(self.settingFileName, 'r') as f:
            
                data = json.load(f)
                return data
        
    #----------------------------------------------------------------------
    def onInit(self):
        
        pass
    #----------------------------------------------------------------------
    def onStart(self):
        pass

    #----------------------------------------------------------------------
    def onStop(self):
        pass 
        
    #----------------------------------------------------------------------
    def onTick(self, tick):
        pass
    
if __name__ == "__main__":
    stategy = PirateStrategy()
    data = stategy.loadStrategySetting()
    print data['selected']
    