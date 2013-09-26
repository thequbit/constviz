import subprocess

def downloadpage(url):
    p = subprocess.Popen(['curl', url], stdout=subprocess.PIPE, 
                                        stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
