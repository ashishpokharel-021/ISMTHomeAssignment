{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "11b40852-b7c5-4a47-a85d-f76f0317e72b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The list is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
      "The sum table is given below :\n",
      "1+2=3\n",
      "3+3=6\n",
      "6+4=10\n",
      "10+5=15\n",
      "15+6=21\n",
      "21+7=28\n",
      "28+8=36\n",
      "36+9=45\n",
      "45+10=55\n",
      "So, the total sum is : 55\n"
     ]
    }
   ],
   "source": [
    "#1.Create a list of the first 10 positive integers. Write a for loop that calculates and prints the sum of all numbers in the list.\n",
    "\n",
    "num=[1,2,3,4,5,6,7,8,9,10]\n",
    "print(\"The list is :\",num)\n",
    "sum=1\n",
    "print(\"The sum table is given below :\")\n",
    "for i in num[1:]:\n",
    "    sum=sum+i\n",
    "    print(f\"{sum-i}+{i}={sum}\")\n",
    "print(\"So, the total sum is :\",sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "26e59284-accd-4065-9d08-9cf18fa1cea2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your list goes like this :\n",
      "1.Intrestellar\n",
      "2.Manjumaal Boys\n",
      "3.Telnet\n",
      "4.Agastya\n",
      "5.Dark\n"
     ]
    }
   ],
   "source": [
    "#2. Create a list of your five favorite movies. Write a for loop that prints each movie along with its position in the list (e.g., \"1. Inception\").\n",
    "movies=['Intrestellar','Manjumaal Boys','Telnet','Agastya','Dark']\n",
    "print(\"Your list goes like this :\")\n",
    "for i in range(len(movies)):\n",
    "    print(f'{i+1}.{movies[i]}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1636d0b9-4243-497d-a957-3f5974cc1b25",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your list is : ['1.2', '3.5', '5.6', '5.5']\n",
      "Your list in double is : [2.4, 7.0, 11.2, 11.0]\n"
     ]
    }
   ],
   "source": [
    "#3. Given a list of strings representing decimal numbers (e.g., ['1.1', '2.2', '3.3']), write a for loop that converts each string to a float, doubles the value, and prints the result.\n",
    "list=[\"1.2\",\"3.5\",\"5.6\",\"5.5\"]\n",
    "double_list=[]\n",
    "print(\"Your list is :\",list)\n",
    "for i in range(len(list)):\n",
    "    double=float(list[i])*2\n",
    "    double_list.append(double)\n",
    "print(\"Your list in double is :\",double_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e4cd5a46-c009-42c5-a55a-8397f1db309c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The list in integer is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]\n",
      "The list in string is : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']\n"
     ]
    }
   ],
   "source": [
    "#4. Create a list of numbers from 1 to 20. Write a for loop that iterates through the list, converts each number to a string, and creates a new list with these string values. Print the new list.\n",
    "list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]\n",
    "string_list=[]\n",
    "print(\"The list in integer is :\",list)\n",
    "for i in range(len(list)):\n",
    "    string=str(list[i])\n",
    "    string_list.append(string)\n",
    "print(\"The list in string is :\",string_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b42f43f5-2902-4da5-a7ca-655beea90a65",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the name afjp'fbga\n",
      "Enter the name bfPSU\n",
      "Enter the name BPSA\n",
      "Enter the name BVAUP\n",
      "Enter the name BVSUI\n",
      "Enter the name ABPU\n",
      "Enter the name BVAUP\n",
      "Enter the name BPIUA\n",
      "Enter the name BVUDA\n",
      "Enter the name BPIUFA\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[\"afjp'fbga\", 'ABPU']\n"
     ]
    }
   ],
   "source": [
    "#5. WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name starts with ‘a’ or ‘A’\n",
    "name=[]\n",
    "list=[]\n",
    "for i in range(10):\n",
    "    names=(input(\"Enter the name\"))\n",
    "    name.append(names)\n",
    "    if(name[i][0]==\"a\" or name[i][0]==\"A\"):\n",
    "        list.append(names)\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f4bbc5a8-7e01-46e3-a414-6790d434ba58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the name gfuqoa\n",
      "Enter the name haiu\n",
      "Enter the name ahuqapha\n",
      "Enter the name gu\n",
      "Enter the name aup\n",
      "Enter the name ghup\n",
      "Enter the name auoauga\n",
      "Enter the name uioggap\n",
      "Enter the name gourg\n",
      "Enter the name iupgq\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['gfuqoa', 'ahuqapha', 'auoauga']\n"
     ]
    }
   ],
   "source": [
    "#6. WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name ends with ‘a’ or ‘A’\n",
    "name=[]\n",
    "list=[]\n",
    "for i in range(10):\n",
    "    names=(input(\"Enter the name\"))\n",
    "    name.append(names)\n",
    "    if(name[i][-1]==\"a\" or name[i][-1]==\"A\"):\n",
    "        list.append(names)\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90c78894-0c9f-452d-bdfa-843b0168f3a5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
