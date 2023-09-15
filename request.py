import re, requests

def extract_nonce(content):
    #with open(file_path, 'r') as file:
        #content = file.read()

        url_pattern =r'data-nonce="\w+"'

        matches = re.findall(url_pattern, content)
        return matches
    

if __name__ == "__main__":
    res = requests.get('https://memoryleaks.ir/wp-login.php')
    #print(res.text)
    print(extract_nonce(res.text)[0])
    #file_path = "./wp-login.php"

    #data = extract_nonce(res.text)
    #print(data[0])


