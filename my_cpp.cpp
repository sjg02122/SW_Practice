#include <iostream>
#include <algorithm>
#include <vector>

class Date {
  int year_;
  int month_;  // 1 부터 12 까지.
  int day_;    // 1 부터 31 까지.
  std::vector<int>month_31;
  std::vector<int>month_30;
 public:
  void SetDate(int year, int month, int date);
  void AddDay(int inc);
  void AddMonth(int inc);
  void AddYear(int inc);

  void ShowDate();
};

void Date::ShowDate()
{
  std::cout<<"YYYY,MM,DD "<<year_ <<","<<month_<<","<<day_;
}
void Date::SetDate(int y, int m , int d)
{
  year_ = y;
  month_ = m;
  day_= d;

  month_31.push_back(1);
  month_31.push_back(3);
  month_31.push_back(5);
  month_31.push_back(7);
  month_31.push_back(8);
  month_31.push_back(10);
  month_31.push_back(12);

  month_30.push_back(4);
  month_30.push_back(6);
  month_30.push_back(9);
  month_30.push_back(11);
  
  
}
void Date::AddMonth(int inc)
{
  month_ +=1;
  if(month_>13)
  {
    year_ +=1;
    month_=1;
  }
}
void Date::AddYear(int inc)
{
  year_+=1;
}

void Date::AddDay(int inc)
{
  day_ +=inc;
  int leap_year = 0;
  std::vector<int>::iterator iter;
  if(year_%4==0)
  {
    if(year_%100==0)
    {
      if(year_%400==0)
      {
        leap_year=1;
      }

    }
    else
    {
      leap_year = 1;
    }
  }
  iter = std::find(month_31.begin(),month_31.end(),month_);
  
  if(iter==month_31.end())
  {
    //30으로 끝나는 경우
    if(month_!=2)
    {
      if(day_>30)
      {
        month_ +=1;
        day_ = day_-30;
      }
    }
    else
    {
      if(leap_year==1)
      {
        if(day_>29)
        {
          day_ = day_-29;
          month_ +=1;
        }
      }
      else
      {
        if(day_>28)
        {
          day_ = day_ -28;
          month_ +=1;
        }
      }
    }
  }
  else
  {
    std::cout<<"여긴가?";
    //31로 끝나는 경우
    if(month_!=2)
    {
      if(day_>31)
      {
        month_ +=1;
        day_ = day_ -31;
        if(month_>12)
        {
          month_ = 1;
          year_+=1;
        }
      }
    }
    else
    {
      if(leap_year==1)
      {
        if(day_>29)
        {
          day_ = day_-29;
          month_ +=1;
        }
      }
      else
      {
        if(day_>28)
        {
          day_ = day_ -28;
          month_ +=1;
        }
      }
    }
    
  }
}

int main(){
  Date a;
  int input_d;
  int input_m;
  int input_y;
  std::cout<<"Set YYYY:";
  std::cin >>input_y;
  std::cout<<"\n";

  std::cout<<"Set MM:";
  std::cin >>input_m;
  std::cout<<"\n";

  std::cout<<"Set DD:";
  std::cin >>input_d;
  std::cout<<"\n";

  a.SetDate(input_y,input_m,input_d);
  a.AddDay(3);
  a.ShowDate();
  return 0;
}