#include <iostream>

using namespace std;

struct node
{
    int data;
    node *next;
};

class LinkedList
{
private:
    node *head, *tail;
    int size;

public:
    LinkedList();
    ~LinkedList();
    int getSize();
    bool isEmpty();
    int getDataAt(int);
    int getDataFromEnd(int);
    int front();
    int back();
    void display();
    void push_front(int);
    void pop_front();
    void push_back(int);
    void pop_back();
    void insert(int ,int);
    void erase(int);
    int erase_value(int);
    void reverse();    
};

LinkedList::LinkedList()
{
    this->head = NULL;
    this->tail = NULL;
    this->size = 0;
}

LinkedList::~LinkedList()
{
    node *i = head;
    while (i != NULL)
    {
        node *temp = i;
        i = i->next;
        delete temp;
    }
}

int LinkedList::getSize()
{
    return this->size;
}

bool LinkedList::isEmpty()
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

int LinkedList::getDataAt(int pos)
{
    if (pos < 0 || pos > size-1)
    {
        return -1;
    }
    else
    {
        node *temp = this->head;
        for (int i = 0; i < pos; i++)
        {
            temp = temp->next;
        }
        return temp->data;        
    }
}

int LinkedList::getDataFromEnd(int pos)
{
    return this->getDataAt(this->size-pos);
}

int LinkedList::front()
{
    return this->head->data;
}

int LinkedList::back()
{
    return this->tail->data;
}

void LinkedList::push_front(int ele)
{
    node *temp = new node();
    temp->data = ele;
    if (this->head == NULL)
    {
        this->head = temp;
        this->tail = temp;
        temp->next = NULL;
    }
    else
    {
        temp->next = this->head;
        this->head = temp;
    }
    this->size++;
}

void LinkedList::push_back(int ele)
{
    node *temp = new node();
    temp->data = ele;
    if (this->tail == NULL)
    {
        this->tail = temp;
        this->head = temp;
        temp->next = NULL;
    }
    else
    {
        this->tail->next = temp;
        this->tail = temp;
        this->tail->next = NULL;
    }
    this->size++;    
}

void LinkedList::pop_front()
{
    if (this->head == NULL)
    {
        cout << "List is empty" << endl;
    }
    else
    {
        node *temp = this->head;
        this->head = this->head->next;
        delete temp;
        if (this->head == NULL) 
        {
            this->tail = NULL;
        }
        this->size--;
    }
}

void LinkedList::pop_back()
{
    if (this->tail == NULL)
    {
        cout << "List is empty" << endl;
    }
    else if (this->head->next == NULL)
    {
        node *temp = this->tail;
        this->tail = NULL;
        this->head = NULL;
        delete temp;
        this->size--;
    }
    else
    {
        node *prev = NULL;
        for (node *i = this->head; i != this->tail; i = i->next)
        {
            prev = i;
        }
        this->tail = prev;
        prev = prev->next;
        this->tail->next = NULL;
        delete prev;
        this->size--;
    }
}

void LinkedList::insert(int pos, int ele)
{
    if (pos == 1)
    {
        this->push_front(ele);
    }
    else if (pos == this->size)
    {
        this->push_back(this->size-1);
    }
    else
    {
        node *prev = this->head;
        node *temp = new node();
        temp->data = ele;
        for (int i = 0; i < pos; i++)
        {
            prev = prev->next;
        }
        temp->next = prev->next;
        prev->next = temp;
    }
}

void LinkedList::erase(int pos)
{

    if (pos == 1)
    {
        this->pop_front();
    }
    else if (pos == this->size)
    {
        this->pop_back();
    }
    else
    {
        node *prev = this->head;
        for (int i = 0; i < pos; i++)
        {
            prev = prev->next;
        }
        node *temp = prev->next;
        prev->next = temp->next;
        delete temp;
    }
}

int LinkedList::erase_value(int ele)
{
    int pos = -1;
    node *temp = this->head;
    node *prev = NULL;
    for (int i = 0; i < this->size; i++)
    {
        if (temp->data == ele)
        {
            pos = i;
            break;
        }
        else
        {
            prev = temp;
            temp = temp->next;
        }   
    }
    prev->next = temp->next;
    delete temp;
    return pos;
}

void LinkedList::reverse()
{
    node *prev = head;
    node *i = head->next;
    while (i != NULL)
    {
        node *temp= i;
        i = i->next;
        temp->next = prev;
        prev = temp;
    }
    this->tail = this->head;
    this->tail->next = NULL;
    this->head = prev;
}

void LinkedList::display()
{
    for (node *i = this->head; i != NULL; i = i->next)
    {
        cout << i->data << endl;
    }
}

int main(int argc, char const *argv[])
{
    LinkedList list;
    
    list.push_front(1);
    list.push_front(2);
    list.push_front(3);
    list.push_front(4);
    
    list.pop_front();
    list.pop_front();
    list.push_front(10);
        
    list.pop_front();
    list.push_back(11);
    list.display();

    list.reverse();
    list.display();

    return 0;
}
