#include <stdio.h>
#include <iostream>
#include <map>

using namespace std;




int main(){
      map<char,int>info;

      for(int ch='a'; ch < 'Z' ; ch++){
            info[ch] = 0;
      }
      string word;
      cin>>word;

      int m = word.length() - 1;
      
      for(int i = 0 ; i <= m ; i++)  info[word[i]] = m - i ; // how far we will shift in a char occurrence

      string Text;      
      cin>>Text;

      int p =0;
      int n = Text.length() ;
      int j = 0;
      while(p + j < n ){
            j = m ;
            while( j >= 0 && word[j] == Text[p + j]) j--; // j = how many char didn't match

            if(j < 0){cout<<"found matching in postion "<<p + 1<<endl; return 0;}  // if j = 0  it means all chars have matched

            if(info[Text[p+j]] == 0) p+=m;
            else{
                  p+=info[Text[p+j]];
            }
      }
      cout<<"No Match found";
}