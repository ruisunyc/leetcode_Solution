class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '::' in IP:return  "Neither"
        if '.' in IP:
            ipv4 = IP.split('.')
            if len(ipv4)!=4:return "Neither"
            for num in ipv4:
                if not num.isdigit():return 'Neither'
                if int(num)<0 or int(num)>255 or (len(num)!=1 and num[0]=='0'):return 'Neither'
            return 'IPv4'
        if ':' in IP:
            ipv6 = IP.split(':')
            if len(ipv6)!=8:return 'Neither'
            for num in ipv6:                
                if len(num)>4 or len(num)<1:return 'Neither'
                for e in num.upper():
                    if not (ord('0')<=ord(e)<=ord('9') or ord('A')<=ord(e)<=ord('F') or ord('a')<=ord(e)<=ord('f')):return 'Neither'                  
            return 'IPv6'
        return 'Neither'
