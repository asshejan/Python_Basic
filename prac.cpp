#include <bits/stdc++.h>
using namespace std;
#define endl "\n"
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
	

	string s;
	cin >> s;
	int l, r;
	l = r = 0;
	string res[1000 / 2];
	int idx = 0;
	string ans;
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == 'L')
		{
			l++;
			ans += 'L';
		}
		else {
			r++;
			ans += 'R';
		}

		if (l == r)
		{
			res[idx] = ans;
			ans = "";
			idx++;
		}

	}
	
	cout << idx << endl;
	for (int i = 0; i < idx; i++){
		cout << res[i] << endl;
    }


    return 0;
}