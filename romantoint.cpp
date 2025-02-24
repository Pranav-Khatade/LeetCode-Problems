//Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

//I can be placed before V (5) and X (10) to make 4 and 9. 
//X can be placed before L (50) and C (100) to make 40 and 90. 
//C can be placed before D (500) and M (1000) to make 400 and 900.
//Given a roman numeral, convert it to an integer.

#include <iostream>
#include <string>
#include <map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        map<char, int> dictionary = {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000} };
        int sum = 0;
        for (size_t i = 0; i < s.length(); i++) {
            if (i + 1 <s.length() && dictionary[s[i]] < dictionary[s[i + 1]]) 
            {
                sum -= dictionary[s[i]];
            }
            else {
                sum += dictionary[s[i]];
            }
            }
        return sum;
    }
};

int main() {
    Solution s1;
    string name;
    cout<<"Enter a Roman numeral: ";
    cin>>name;
    int result =s1.romanToInt(name);
    cout<<result<<endl;
    return 0;
}
