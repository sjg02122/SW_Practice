#include <iostream>
#include <vector>
#include <string>

using namespace std;

char board[5][5];
bool inRange(int x, int y);
bool hasWord_for(int x, int y, const string& word);
bool hasWord_recursive(int x, int y, const string& word);

const int dx[8] = { -1,-1,-1,1,1,1,0,0 };
const int dy[8] = { -1 ,0 , 1, -1, 0 ,1,-1,1 };


int main()
{
	string word;
	char board_input;

	cout << "input your word : ";
	cin >> word;
	
	cout << "input your board : \n";
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			cin >> board_input;
			board[i][j] = board_input;
		}
	}

	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			if (hasWord_recursive(i, j, word))
			{
				cout << "There is the word that you find : " << word << endl;
				return 0;
			}
		}
	}
	
	cout << " There is no word that you find ! " << endl;
	return 0;
}

void stack_print(const vector<int> temp)
{
	vector <int> temp2 = temp;
	for (int i=0 ; i< temp2.size();i++)
	{
		cout << temp2.back() << " ";
		temp2.pop_back();
	}
	cout << endl;
}

bool inRange(int x, int y)
{
	if (x >= 5 || x < 0 || y >= 5 || y < 0)
	{
		return false;
	}
	return true;
}

bool hasWord_for(int x, int y, const string& word)
{
	cout << "Input location : " << x << " " << y << endl;
	int word_length = word.size();
	bool ans = false;
	int cnt = 0;
	vector <int> stack_x;
	vector <int> stack_y;
	
	if (word.size() == 1)
	{
		if (word[0] != board[x][y])
		{
			return false;
		}
		return true;
	}

	if (word[0] != board[x][y])
	{
		return 0;
	}
	else
	{

		stack_x.push_back(x);
		stack_y.push_back(y);
		vector <int> next_stack_x;
		vector <int> next_stack_y;
		int visited[5][5] = { 0, };
		visited[x][y] = 1;
		next_stack_x.push_back(x);
		next_stack_y.push_back(y);
		while (!next_stack_x.empty() && !next_stack_y.empty())
		{
			cnt+=1;
			//cout <<"Cnt  " << cnt << endl;
			next_stack_x = {};
			next_stack_y = {};

			while (!stack_x.empty() && !stack_y.empty())
			{

				int cur_x = stack_x.back();
				int cur_y = stack_y.back();
				//cout << "Cur x,y " << cur_x << cur_y << endl;

				stack_x.pop_back();
				stack_y.pop_back();

				for (int i = 0; i < 8; i++)
				{
					int nx = cur_x + dx[i];
					int ny = cur_y + dy[i];
					if (!inRange(nx, ny))
					{
						continue;
					}
					if ((board[nx][ny] != word[cnt]) || (visited[nx][ny]!=0))
					{
						continue;
					}					
					if (cnt == word.size()-1 && board[nx][ny] == word[cnt])
					{
						return true;
					}

					//cout << " Nx,Ny,val " << nx << ' ' << ny << " " << board[nx][ny] << endl;
					next_stack_x.push_back(nx);
					next_stack_y.push_back(ny);	
					visited[nx][ny] = 1;
				}
			}
			stack_x = next_stack_x;
			stack_y = next_stack_y;


		}
		return false;
	}
}

bool hasWord_recursive(int x, int y, const string& word)
{
	if (!inRange(x, y))
	{
		return false;
	}

	if (board[x][y] != word[0])
	{
		return false;
	}

	if (word.size() == 1)
	{
		return true;
	}

	for (int d = 0; d < 8; d++)
	{
		int nx = x + dx[d];
		int ny = y + dy[d];
		if (hasWord_recursive(nx, ny, word.substr(1)))
		{
			return true;
		}
	}

	return false;
}
