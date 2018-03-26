##from multiprocessing import Pool
import bs4 as bs
import requests

class Local_web_links():
    """
        This is a one threaded class to find all the local
        or global links - a spider as some call it
        local links - the website links
        It is possible to use pool - multiprocessing in order
        to make it run faster, but it will be nosier as you pass
        a lot of request to the server
    """

    def __init__(self, base_url, clean_url,
                 headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}):

        self.base_url = base_url
        self.clean_url = clean_url
        self.headers = headers

    def start(self):
        """ Start to find the links of the website """
        
        print('Strating... URL : ' + self.base_url)
        local_links, global_links = self.get_links(self.base_url)
        print(local_links)
        print('Local links in ' + self.base_url +' : '+ str(len(local_links)))

        links_to_visit = [] + local_links # Diffrent memory address from local_links
        temp_links = [] # Hold the new links to visit
        links = local_links # All the links, same memory address as local_links

        # If there are links to visit
        # Then iterate throught them
        # Each time add new links that are not in the total link
        # list - links, to the temp_links
        # After the all iteration in links_to_vist, set it to
        # the temp_links list that contain the new links to vist
        # and then empty temp_links
        while(links_to_visit):
            for link in links_to_visit:
                links, to_visit = self.clean_list(links, self.get_links(link)[0])
                print('URL : ' + link + ' , new local links : '+ str(len(to_visit)))
                temp_links = temp_links + to_visit
            links_to_visit = temp_links
            temp_links = []

            print('\n\n')
            print('Links to visit : ' + str(len(links_to_visit)))
            print('\n\n')

        # Print all the links
        print('Website : ' + self.base_url)
        print('Total local links : ' + str(len(links)))
        print('\n\n')
        for link in links:
            print(link)

    def get_links(self, url):
        """
            Return the local and the global links as [local list, global list]
            Links that can be raed from the html of the page
            Tags - <a herf>, <form action>
            local links are the website links
            global are general sites that found
        """
        
        local_links = []
        global_links = []
        page_id = ['cookies'] # List that contain the page attribute id and name
                              # for each tag that have them
                              # need it for the # reference
        
        # Get the html body, and check if the status is 200 - page found
        r = requests.get(url, headers=self.headers)
        if(r.status_code != 200):
            return [[],[]]
        soup = bs.BeautifulSoup(r.text, 'html5lib')
        soup = soup.body
        # If there is no html body
        if(soup == None):
            return [[],[]]
        
        # If the url do not end with / add it to create organized data
        if(url[-1] != '/'):
            url = url + '/'

        # Get the id and name attributes
        for tag_id in soup.find_all(id=True,name=True):
            id_name = tag_id.get('id')
            tag_name = tag_id.get('name')
            if(id_name != None):
                if(not(id_name in page_id)):
                    page_id.append(id_name)
            elif(tag_name != None):
                if(not(tag_name in page_id)):
                    page_id.append(tag_name)

        # Next two blocks of code can be same method
        # but there is a lot of iterations so it will be
        # a little more slower because the cost involved in calling a funtion

        # Iterate and find all the a tags
        # For each get the link - href
        # use without_pound to clear the url from # reference
        # Checks if the link is not empty or mail
        # Link that are local appended to local_links
        # and the global to global_links
        # Apeend them if they are not exist yet in the list
        for link in soup.find_all('a'):
            temp_link = link.get('href')
            temp_link = self.without_pound(temp_link, page_id)
            if(temp_link != 'None' and (not temp_link.startswith('mailto'))):
                local_link = self.handle_local_link(url, temp_link)
                if(local_link != 0):
                    if(not(local_link in local_links)):
                        local_links.append(local_link)
    # saves memory - local likes are needed
    #            else:
    #                if(not(temp_link in global_links)):
    #                    global_links.append(temp_link)

        # Same as above just it is in form tags
        # and the links are in the action variable
        
        for link in soup.find_all('form'):
            temp_link = link.get('action')
            temp_link = self.without_pound(temp_link, page_id)
            if(temp_link != 'None' and (not temp_link.startswith('mailto'))):
                local_link = self.handle_local_link(url, temp_link)
                if(local_link != 0):
                    if(not(local_link in local_links)):
                        local_links.append(local_link)
    # saves memory - local likes are needed
    #            else:
    #                if(not(temp_link in global_links)):
    #                    global_links.append(temp_link)

        return [list(set(local_links)), list(set(global_links))]

    def without_pound(self, link, page_id):
        """
            Check if the link is not None and remove the # for it
            retrun None as string or the new link
            #hello return None 
            http://docs.python-requests.org/en/master/#aaa return
            http://docs.python-requests.org/en/master/
            handle links with javascript code as well
        """
        
        # No link in the tag - link.get return a None
        if(link == None):
            return 'None'
        
        lenght = len(link)

        # Empty link
        if(lenght == 0):
            return 'None'

        # Same page
        if(link[0] == '#'):
            return 'None'

        # Javascript code
        if(link.startswith('javascript:')):
            return 'None'
        
        # Check if the lenght is greater then 2
        # Link that are '/' - like an like empty link
        lenght = lenght - 1
        if(lenght != 0):
            if(link[lenght-1] == '/'):
                lenght = lenght - 1
        else:
            return 'None'
        
        # Go until the first #
        # If it get to / so # is no longer relevant to check
        # If after the / is java script code, remove it from url
        # After the while loop if before the # is a / return the link without it
        # Example - website.com/abc/#hello - website.com/abc/
        # Else if before it .html or .htm return the link without # and the string
        # after it
        # Else if the string after the # is an id of a name attribute from page_attr
        # remove the # with the string after it
        # Else it a char as part of the link
        while(link[lenght] !='#' and lenght > -1):
            if(link[lenght] == '/'):
                if(link[lenght+1:].startswith('javascript:')):
                    return link[:lenght+1]
                else:
                    return link
            lenght = lenght - 1
        # Went throwout the link and didnt find a #
        if(lenght == - 1):
            return link
                
        if(link[lenght-1] == '/'):
            return link[:lenght]
        elif(link[:lenght].endswith('.html') or link[:lenght].endswith('.htm')):
            return link[:lenght]
        elif(link[lenght+1:] in page_id):
            return link[:lenght]
        else:
            return link


    def handle_local_link(self, url, link):
        """
            Check if the link is local a website link
            return the link accordingly
        """
        
        # If the url dont end with / - add the '/' to it
        if(url[-1] != '/'):
            url = url + '/'

        # If link starts with / - go to the root web and add it
        # Example - website.com/abc/hello link - /great
        # Return - website.com/great
        if(link.startswith('/')):
            return self.base_url + link[1:]
        # ../ is back dir
        elif(link.startswith('../')):
            return self.back_link(url, link)
        # ./ back dir for file ending in the url
        # such as .html .asp .php
        elif(link.startswith('./')):
             link = '.' + link
             return back_link(url, link)
        check_same_web = self.same_web(url, link)
        if(check_same_web == 2): # The link is clear start as hello/great
            return self.handle_files(url, link)
        elif(check_same_web == 1):
            return link
        else:
            return 0 # global link

        return [list(set(local_links)), list(set(global_links))]

    def same_web(self, url, link):
        """
            Check if it same website
            return 0 if not
            return 1 if it is with http or https beginning
            return 2 if it is a local link like folder_name/file
        """
        
        # Clean link - refer to the folder or file of the website
        if(not(link.startswith('http://') or link.startswith('https://'))):
            return 2

        # Clean the link from http or https
        if(link.startswith('http://')):
            link = link[7:]
            url = self.clean_url
        elif(link.startswith('https://')):
            link = link[8:]
            url = self.clean_url

        # Check if the base url is bigger then the link - maybe it is
        # the same website
        lenght_b = len(url)
        lenght_l = len(link)
        if(lenght_b > lenght_l):
            return 0

        # Compere them if they are same string, same as a in b
        # The link that get here start with http or https
        # cleaned them from http or https 2 blocks up
        # website.com - website.com/hello same website
        l = 0
        while(l < lenght_b):
            if(url[l] != link[l]):
                return 0
            l = l + 1
        return 1

    def back_link(self, url, link):
        """
            Back directory acorrding the numbers of ../
            Example - website.com/hello/great/ , ../great2
                      website.com/hello/great2/
            or if the are a lot of ../
            Example - website.com/hello/great/ , ../../../great2
                      website.com/great2/
        """

        # Count the ../ in the link
        back_dir = 0
        i = 0
        lenght = len(link)
        while(i < lenght):
            if(link[i:i+3] == '../'):
                back_dir = back_dir + 1
                i = i + 3
            else:
                break
            
        if(back_dir > 0 and url.endswith(self.clean_url)):
            return url + link[back_dir*3:]

        # For each ../ goes back directoriy
        check_back = 0
        lenght = len(url) - 2 # first / is the end of the url
        while(lenght > -1):
            if(check_back != back_dir):
                if(url[lenght] == '/'):
                    check_back = check_back + 1
                lenght = lenght - 1
            else:
                break

        return url[:lenght+1] + link[back_dir*3 - 1:]

    def handle_files(self, url, link):
        """
            Check if the url end with a .filetype
            if it is take it back 1 dir and return it
            Else return url + link
            Example: url - website.com/hello/great.html
                     link - web.php
                     return - website.com/hello/web.php
        """
        
        files = ['.html', '.htm', '.php', '.jpg', '.jepg', '.asp',
                 '.aspx']
        
        # Remove the / from the end
        if(url[-1] == '/'):
            url = url[:-1]

        for file in files:
            if(url.endswith(file)):
                link = '../' + link
                url = url + '/'
                return self.back_link(url, link)

        url = url + '/'
        return url + link

    def clean_list(self, all_links, new_links):
        """
            Add new items from new_links to all_links
            Return a list with the old and new links
            and the new links there werent in all_links
        """
        
        # Take each item in new_links, check if
        # it doesnt exit in all links - add it to all_links
        # and to the to_visit list
        to_visit = []
        for i in new_links:
            if(i not in all_links):
                to_visit.append(i)
                all_links.append(i)

        return all_links, to_visit

if __name__ == '__main__':
    
    local_links = Local_web_links('https://sites.envato.com/', 'sites.envato.com/')
    local_links.start()          
