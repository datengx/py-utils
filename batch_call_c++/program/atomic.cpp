#include <iostream>
#include <string>

using namespace std;
int main(int argc, char *argv[]) {
	if (argc > 1) {
		string str = string(argv[1]);
		cout << str << endl;
	}
	return 0;
}