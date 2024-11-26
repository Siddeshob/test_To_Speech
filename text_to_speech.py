import pyttsx3
import time

def speak_words(words):

    engine=pyttsx3.init()

    engine.getProperty('rate')
    engine.setProperty('rate',160)
    value=0
    for w in words:
        value+=1
        print(f'words are {time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec} {value}: {w}')
        time.sleep(4)
        engine.say(w)
        engine.runAndWait()
        
        

words=['1001','helllo','siddesha','car','house']
set1=['Request', 'configuration', 'setup', 'installation', 'integration', 'system', 'network', 'connectivity', 'debug', 'testing', 'logs', 'maintenance', 'deployment', 'access', 'permission', 'credentials', 'backup', 'restore', 'compatibility', 'monitoring', 'ticket', 'software', 'hardware', 'tool', 'patch', 'error', 'bug', 'diagnostics', 'fix', 'solution', 'query resolution', 'performance', 'optimization']
set2=['Assistance', 'guidance', 'resolution', 'response', 'query', 'clarification', 'explanation', 'troubleshooting', 'help', 'follow-up', 'priority', 'escalation', 'requirement', 'improvement', 'feedback', 'suggestion', 'workflow', 'solution', 'issue', 'task', 'response time', 'service', 'efficiency', 'support ticket', 'communication', 'update', 'process', 'documentation', 'report', 'recovery', 'verification', 'resource', 'collaboration']
set3=['Screen', 'share', 'display', 'file', 'folder', 'document', 'presentation', 'dashboard', 'database', 'update', 'error', 'debug', 'command', 'upload', 'download', 'execute', 'permission', 'data', 'code', 'function', 'API', 'backend', 'frontend', 'test', 'bug', 'fix', 'log', 'configuration', 'setup', 'result', 'output', 'input', 'format', 'version', 'repository', 'terminal', 'deploy', 'automation', 'variable', 'integration', 'environment']
set4=['Meeting', 'agenda', 'discussion', 'report', 'update', 'project', 'deadline', 'review', 'task', 'assignment', 'feedback', 'suggestion', 'improvement', 'performance', 'colleague', 'manager', 'request', 'support', 'process', 'documentation', 'approval', 'issue', 'solution', 'status', 'plan', 'completion', 'communication', 'implementation', 'schedule', 'priority', 'reminder', 'announcement', 'note', 'summary', 'goal', 'responsibility']
speak_words(set2)