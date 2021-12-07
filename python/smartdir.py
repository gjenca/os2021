import json

class SmartDir:

    def __init__(self,dirname):

        self.dirname=dirname

    def __getitem__(self,filename):

        with open(self.dirname+'/'+filename) as f:
            return json.loads(f.read())


    def __setitem__(self,filename,value):
        fnm=self.dirname+'/'+filename 
        with open(fnm,'w') as f:
            f.write(json.dumps(value))


