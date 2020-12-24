#include <iostream>
#include <array>
#include <vector>

using namespace std;

class IntArray
{
private:
	int m_length = 0;
	int* m_data = nullptr;

public:
	//Constructors
	//Destructors
	//initialize()
	//reset()
	//resize()
	//insertBefore(const int & value, const int & ix);
	//remove(const int & ix)
	//push_back(const int & value);
	IntArray()
	{}

	IntArray(const int& length_in)
		:m_length(length_in)
	{
		m_data = new int[length_in];
	}
	~IntArray()
	{
		delete[] m_data;
	}
	IntArray(const std::initializer_list<int>& list)
		:IntArray(list.size())
	{
		int count = 0;
		for (auto& element : list)
		{
			m_data[count] = element;
			++count;
		}
	}
	void reset()
	{
		delete[] m_data;
		m_data = nullptr;
		m_length = 0;
	}

	IntArray &  resize(const int & length_in)
	{
		if (m_length == length_in)
		{
			return *this;
		}
		else
		{
			int* temp = new int[length_in];

			if (m_length < length_in)
			{
				for (int i = 0; i < m_length; i++)
				{
					temp[i] = m_data[i];
				}
				for (int i = m_length; i < length_in; i++)
				{
					temp[i] = 0;
				}
			}
			else
			{
				for (int i = 0; i < length_in; i++)
				{
					temp[i] = m_data[i];
				}
			}
			m_length = length_in;
			delete[] m_data;
			m_data = temp;
		}
		return *this;
	}
	IntArray& insertBefore(const int& value, const int& ix)
	{
		resize(m_length + 1);
		int temp = 0;
		for (int i = m_length-2; i > ix-1; i--)
		{
			m_data[i+1] = m_data[i];
		}
		m_data[ix] = value;
		return *this;
	}

	//remove(const int & ix)
	//push_back(const int & value);

	IntArray& remove(const int& ix)
	{
		for (int i = ix; i < m_length; i++)
		{
			m_data[i] = m_data[i + 1];
		}
		m_length -= 1;
		resize(m_length);

		return *this;
	}

	IntArray& push_back(const int& value) 
	{
		resize(m_length + 1);
		m_data[m_length - 1] = value;

		return *this;
	}


	friend std::ostream& operator << (std::ostream& out, const IntArray& intarr)
	{
		for (int i = 0; i < intarr.m_length; i++)
		{
			out << intarr.m_data[i]<<" ";
		}
		return out;
	}

	IntArray& operator =(const std::initializer_list<int>& list)
	{
		delete[] m_data;
		m_length = list.size();
		m_data = new int[m_length];

		int count = 0;
		for (auto& element : list)
		{
			m_data[count] = element;
			count++;
		}
		return *this;
	}

	IntArray& operator =(const IntArray& copy_intarr)
	{
		if (this == &copy_intarr)
		{
			return *this;
		}
		delete[] m_data;

		m_length = copy_intarr.m_length;

		if (copy_intarr.m_data != nullptr) {
			m_data = new int[m_length];
			for (int i = 0; i < m_length; i++)
			{
				m_data[i] = copy_intarr.m_data[i];
			}
		}
		else
		{
			m_data = nullptr;
		}
		return *this;
	}


};

int main()
{
	IntArray my_arr{1 ,3 ,5, 7, 9};
	IntArray my_arr2;
	cout << my_arr << endl;
	my_arr.insertBefore(10,1);
	cout << my_arr << endl;
	my_arr.remove(3);
	cout << my_arr << endl;
	my_arr.push_back(13);
	cout << my_arr2 << endl;
	cout << my_arr << endl;
	my_arr2 = my_arr;
	my_arr.reset();
	cout << my_arr << endl;
	cout << my_arr2 << endl;
	my_arr.push_back(5);
	my_arr.push_back(5);
	cout << my_arr << endl;

	return 0;
}
