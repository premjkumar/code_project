import sys
import os
from os import walk
import mmap
 
def main():
    print("######Enter the string to search, type quit to exit#######")
    print("######Custom File Search tool ######")
    # input_dir=input("Enter the Directory to search:")
    # searchp(input_dir)
    try:
        if (sys.argv[1] == ""):

            raise IndexError
            #sys.exit
        else:

            input_dir = sys.argv[1]
            datamap = searchPrompt().object_loader(input_dir)
            searchPrompt().receiver(datamap)

    except IndexError:
        print("Please proivide directory path as argument")


#Object class
class searchPrompt():
    def object_loader(self, mypath):
        list_mmap=dict()
        dict_list=[]
        os.chdir(mypath)
        for (dirpath, dirnames, filenames) in walk(mypath):
            for j in range(len(filenames)):
                with open(filenames[j], mode="r", encoding="utf8") as file_obj:
                    with mmap.mmap(file_obj.fileno(),
                                   length=0,
                                   access=mmap.ACCESS_READ) as mmap_obj:
                        
                        list_mmap={f"file_names{j}":[],f"objects{j}":[],f"contents{j}":[j]}
                        list_mmap["file_names{}".format(j)].append(filenames[j])
                        list_mmap["objects{}".format(j)].append(mmap_obj)
                        list_mmap["contents{}".format(j)].append(mmap_obj.read())
                        dict_list.append(list_mmap)
        return(dict_list)                
                        

    def receiver(self, ld_obj):
      
        for i in range(1000000):
            input_str = input("search$>")
            if input_str=="quit":
              break

            else:
              word_list = input_str.split()
              for word in word_list:
                self.counter(ld_obj, word,input_str)
    
    def counter(self, ld_obj, sub_string,input_str): 
        s_list=dict()
        dic_list=[]
        string1=sub_string
        counter=0
        for i in range(len(ld_obj)):
          dict1=ld_obj[i]
          filename=str(dict1[f"file_names{i}"])
          file1=str(dict1[f"contents{i}"])  
          counter=file1.count(string1)
          s_list={"file":[],"count":[]}
          s_list["file"].append(filename)
          s_list["count"].append(counter) 
          dic_list.append(s_list)
        self.ranker(dic_list,input_str)    
         

    def ranker(self,dic_list,input_str):
        d_set={}
        sor_list=[]
        for i in range(len(dic_list)):
          
          dict2=dic_list[i]
          #print(dict2)
          file=dict2[f"file"]
          count=dict2[f"count"]
          #removing brackets
          con=str(count)[1:-1]
          ## percentage logic out of 100 words in the file
          ##
          c_int=round(((int(con)/100)*100))
          f_out=str(file)[1:-1]
          f_ou=str(f_out)[1:-1]
          f_o=str(f_ou)[1:-1]
          file_out=str(f_o)[1:-1]
          #print(con,file_out)
          d_set[file_out] = c_int
        
          #print(d_set)
        res_sor=sorted(d_set.items(), key=lambda t: t[1],reverse=1)
        #print(res_sor)
        
        n_items = res_sor[:10]
        sor_list.extend(n_items)
        self.comparison(sor_list,input_str)
        #print(n_items)



          # sorting the Order
  
         
    def comparison(self,sor_list,input_str):
       
       last_list=[]
 
     
       def iterFlatten(root):
         if isinstance(root, (list, tuple)):
          for element in root:
            for e in iterFlatten(element):
                yield e
         else:
          yield root

       last_list=(list(iterFlatten(sor_list)))
       #print(last_list)
       word_list=input_str.split()
       for word in word_list:
        for it_1 in last_list[:12]:
          print(it_1)
                    
           
  

# Main function calling
if __name__ == "__main__":
    main()
