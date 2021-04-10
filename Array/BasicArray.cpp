#include <iostream>

using namespace std;

class BasicArray
{
private:
    int *arr;
    int size;
    int capacity;
    void resize(int capacity);

public:
    BasicArray(int capacity);
    ~BasicArray();
    int getSize();
    int getCapacity();
    bool isEmpty();
    void push(int ele);
    void insert(int pos, int ele);
    void del(int pos);
    void remove(int ele);
    int get(int pos);
    void getAll();
};

BasicArray::BasicArray(int capacity)
{
    this->capacity = capacity;
    this->arr = new int[capacity];
    this->size = 0;
}

BasicArray::~BasicArray()
{
    delete this->arr;
}

int BasicArray::getSize()
{
    return this->size;
}

int BasicArray::getCapacity()
{
    return this->capacity;
}

bool BasicArray::isEmpty()
{
    if (this->size == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void BasicArray::resize(int capacity)
{
    if (capacity != 0)
    {
        int *temp = new int[capacity];
        for (int i = 0; i < this->size; i++)
        {
            temp[i] = this->arr[i];
        }
        delete arr;
        this->arr = temp;
        this->capacity = capacity;
    }
}

void BasicArray::push(int ele)
{
    if (this->size == this->capacity)
    {
        this->resize(this->capacity * 2);
        this->push(ele);
    }
    else
    {
        this->arr[this->size] = ele;
        this->size++;
    }
}

void BasicArray::insert(int pos, int ele)
{
    if (this->size == this->capacity)
    {
        this->resize(this->capacity * 2);
        this->insert(pos, ele);
    }
    else
    {
        int cur, prev = this->arr[pos];
        for (int i = pos + 1; i <= this->size; i++)
        {
            cur = this->arr[i];
            this->arr[i] = prev;
            prev = cur;
        }
        this->arr[pos] = ele;
        this->size++;
    }
}

void BasicArray::del(int pos)
{
    if (pos < 0 || pos >= this->size)
    {
        cout << "Out of Bounds" << endl;
    }
    else
    {
        for (int i = pos; i < this->size; i++)
        {
            arr[i] = arr[i + 1];
        }
        this->size--;
        if (this->size <= this->capacity / 4)
        {
            this->resize(this->capacity / 2);
        }
    }
}

void BasicArray::remove(int ele)
{
    int pos;
    bool flag = false;
    for (int i = 0; i < this->size; i++)
    {
        if (this->arr[i] == ele)
        {
            pos = i;
            flag = true;
            break;
        }
    }
    if (flag)
    {
        this->del(pos);
    }
    else
    {
        cout << "Element not found" << endl;
    }
}

int BasicArray::get(int pos)
{
    if (pos < 0 || pos >= this->size)
    {
        return -1;
    }
    else
    {
        return arr[pos];
    }
}

void BasicArray::getAll()
{
    for (int i = 0; i < this->size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main(int argc, char const *argv[])
{
    BasicArray obj(5);
    obj.push(10);
    obj.push(11);
    obj.push(12);
    obj.push(13);
    obj.push(14);
    obj.push(15);
    obj.getAll();
    obj.insert(3, 20);
    obj.getAll();
    int ele = obj.get(2);
    cout << ele << endl;
    obj.del(2);
    obj.getAll();
    obj.remove(20);
    obj.getAll();
    obj.push(16);
    obj.getAll();
    obj.del(2);
    obj.del(3);
    obj.del(1);
    obj.del(1);
    obj.del(0);
    obj.del(0);
    obj.del(0);
    obj.getAll();
    obj.push(10);
    obj.getAll();
    obj.del(0);
    obj.getAll();
    obj.push(10);
    obj.getAll();
    obj.push(10);
    obj.push(11);
    obj.push(12);
    obj.push(13);
    obj.push(14);
    obj.push(15);
    return 0;
}
