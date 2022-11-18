{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "090de0bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     fixed acidity;\"volatile acidity\";\"citric acid\";\"residual sugar\";\"chlorides\";\"free sulfur dioxide\";\"total sulfur dioxide\";\"density\";\"pH\";\"sulphates\";\"alcohol\";\"quality\"\n",
      "0      7.4;0.7;0;1.9;0.076;11;34;0.9978;3.51;0.56;9.4;5                                                                                                                     \n",
      "1      7.8;0.88;0;2.6;0.098;25;67;0.9968;3.2;0.68;9.8;5                                                                                                                     \n",
      "2     7.8;0.76;0.04;2.3;0.092;15;54;0.997;3.26;0.65;...                                                                                                                     \n",
      "3     11.2;0.28;0.56;1.9;0.075;17;60;0.998;3.16;0.58...                                                                                                                     \n",
      "4      7.4;0.7;0;1.9;0.076;11;34;0.9978;3.51;0.56;9.4;5                                                                                                                     \n",
      "...                                                 ...                                                                                                                     \n",
      "1594  6.2;0.6;0.08;2;0.09;32;44;0.9949;3.45;0.58;10.5;5                                                                                                                     \n",
      "1595  5.9;0.55;0.1;2.2;0.062;39;51;0.99512;3.52;0.76...                                                                                                                     \n",
      "1596  6.3;0.51;0.13;2.3;0.076;29;40;0.99574;3.42;0.7...                                                                                                                     \n",
      "1597  5.9;0.645;0.12;2;0.075;32;44;0.99547;3.57;0.71...                                                                                                                     \n",
      "1598  6;0.31;0.47;3.6;0.067;18;42;0.99549;3.39;0.66;...                                                                                                                     \n",
      "\n",
      "[1599 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "data=pd.read_csv('C:\\\\Users\\\\exam2\\\\Desktop\\\\winequality-red.csv')\n",
    "print(data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7b62c486",
   "metadata": {},
   "source": [
    "2.\tConvert it to numPy array, name it as wines (leave the first row of the list) and specify the data type of array as float.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "79a4dc4e",
   "metadata": {},
   "source": [
    "import numpy as np\n",
    "wine=np.genfromtxt('C:\\\\Users\\\\exam2\\\\Desktop\\\\winequality-red .csv',delimiter=';',skip_header=1,dtype=float)\n",
    "print(wine)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cb169e79",
   "metadata": {},
   "source": [
    "3.\tIdentify the shape of the array.\n",
    "4.\tDisplay the element at row 3 and column 4.\n",
    "5.\t Display the first three items from the fourth column.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "0cb32993",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1599, 12)\n",
      "2.3\n",
      "[0.   0.   0.04]\n"
     ]
    }
   ],
   "source": [
    "print(np.shape(wine))\n",
    "print(wine[2][3])\n",
    "print(wine[:3,2])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2da6e74e",
   "metadata": {},
   "source": [
    "6.\tDisplay third column from each row."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "e82f96e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1.9 2.6 2.3 ... 2.3 2.  3.6]\n"
     ]
    }
   ],
   "source": [
    "print(wine[:,3])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "703ab4fa",
   "metadata": {},
   "source": [
    "7.\tDisplay fourth row."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "2b325dba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 7.4     0.7     0.      1.9     0.076  11.     34.      0.9978  3.51\n",
      "  0.56    9.4     5.    ]\n"
     ]
    }
   ],
   "source": [
    "print(wine[4])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc5d2228",
   "metadata": {},
   "source": [
    "8.\tAssign value 10 to 2nd row and 6th column element."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "ec1d5868",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 7.8     0.88    0.      2.6     0.098  10.     67.      0.9968  3.2\n",
      "  0.68    9.8     5.    ]\n"
     ]
    }
   ],
   "source": [
    "wine[1,5]=10\n",
    "print(wine[1])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "192f3c6e",
   "metadata": {},
   "source": [
    "9.\tTake the 10th column from wines array and name that slice as slice_new and assign value 666 to all elements of slice_new."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "eef5b6a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.56 0.68 0.65 ... 0.75 0.71 0.66]\n",
      "[666. 666. 666. ... 666. 666. 666.]\n",
      "[666. 666. 666. ... 666. 666. 666.]\n"
     ]
    }
   ],
   "source": [
    "slice_new=wine[:,9]\n",
    "print(slice_new)\n",
    "slice_new[:]=666;\n",
    "print(slice_new)\n",
    "print(wine[:,9])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "316d0ba4",
   "metadata": {},
   "source": [
    "10.\tDisplay wines array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "483c34c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[7.40e+00 7.00e-01 0.00e+00 ... 6.66e+02 9.40e+00 5.00e+00]\n",
      " [7.80e+00 8.80e-01 0.00e+00 ... 6.66e+02 9.80e+00 5.00e+00]\n",
      " [7.80e+00 7.60e-01 4.00e-02 ... 6.66e+02 9.80e+00 5.00e+00]\n",
      " ...\n",
      " [6.30e+00 5.10e-01 1.30e-01 ... 6.66e+02 1.10e+01 6.00e+00]\n",
      " [5.90e+00 6.45e-01 1.20e-01 ... 6.66e+02 1.02e+01 5.00e+00]\n",
      " [6.00e+00 3.10e-01 4.70e-01 ... 6.66e+02 1.10e+01 6.00e+00]]\n"
     ]
    }
   ],
   "source": [
    "print(wine)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a6b57e76",
   "metadata": {},
   "source": [
    "11.\tFind the data type of wines array and Change the data type to int."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "93311c13",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "float64\n",
      "[[  7   0   0 ... 666   9   5]\n",
      " [  7   0   0 ... 666   9   5]\n",
      " [  7   0   0 ... 666   9   5]\n",
      " ...\n",
      " [  6   0   0 ... 666  11   6]\n",
      " [  5   0   0 ... 666  10   5]\n",
      " [  6   0   0 ... 666  11   6]]\n"
     ]
    }
   ],
   "source": [
    "print(wine.dtype)\n",
    "wine=np.array(wine,dtype=int)\n",
    "print(wine)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a4d0151",
   "metadata": {},
   "source": [
    "12.\tAdd 10 points to each quality score."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "3fb6fd2e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5 5 5 ... 6 5 6]\n",
      "[15 15 15 ... 16 15 16]\n"
     ]
    }
   ],
   "source": [
    "print(wine[:,-1])\n",
    "wine[:,-1]+=10\n",
    "print(wine[:,-1])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "274c471a",
   "metadata": {},
   "source": [
    "13.\tFind the sum of all the elements in an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "c8848735",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total sum is: 1226388\n",
      "Row sum is : [746 779 771 ... 773 777 765]\n",
      "col sun is : [  12589      24       1    3350       0   25367   74301      81    4770\n",
      " 1064934   15969   25002]\n"
     ]
    }
   ],
   "source": [
    "print(\"Total sum is:\",np.sum(wine))\n",
    "print(\"Row sum is :\",np.sum(wine,1))\n",
    "print(\"col sun is :\",np.sum(wine,0))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "198cb5d9",
   "metadata": {},
   "source": [
    "16.\tAdd the quality column to itself."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "89ce2be7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[15 15 15 ... 16 15 16]\n",
      "[30 30 30 ... 32 30 32]\n"
     ]
    }
   ],
   "source": [
    "print(wine[:,-1])\n",
    "wine[:,-1]+=wine[:,-1]\n",
    "print(wine[:,-1])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "831c733f",
   "metadata": {},
   "source": [
    "17.\tMultiply alcohol by quality."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "d5784e71",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[270 270 270 ... 352 300 352]\n"
     ]
    }
   ],
   "source": [
    "print(wine[:,-2]*wine[:,-1])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3940be0",
   "metadata": {},
   "source": [
    "18.\tDisplay which wines have a quality rating higher than 5."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "b32ff719",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[  7   0   0 ... 666   9  30]\n",
      " [  7   0   0 ... 666   9  30]\n",
      " [  7   0   0 ... 666   9  30]\n",
      " ...\n",
      " [  6   0   0 ... 666  11  32]\n",
      " [  5   0   0 ... 666  10  30]\n",
      " [  6   0   0 ... 666  11  32]]\n"
     ]
    }
   ],
   "source": [
    "print(wine[wine[:,-1]>5])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "95c2c9fe",
   "metadata": {},
   "source": [
    "19.\tCheck if any wines have a quality rating equal to 10."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "57d63c3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "print(wine[wine[:,-1]==10])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b5326140",
   "metadata": {},
   "source": [
    "20.\tSelect rows in wines where the quality is over 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "c990538e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[  7   0   0 ... 666   9  30]\n",
      " [  7   0   0 ... 666   9  30]\n",
      " [  7   0   0 ... 666   9  30]\n",
      " ...\n",
      " [  6   0   0 ... 666  11  32]\n",
      " [  5   0   0 ... 666  10  30]\n",
      " [  6   0   0 ... 666  11  32]]\n"
     ]
    }
   ],
   "source": [
    "print(wine[wine[:,-1]>7])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cc52b96f",
   "metadata": {},
   "source": [
    "21.\tDisplay wines with alcohol greater than 10 and quality greater than 7."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "a56024e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[False False False ...  True False  True]\n"
     ]
    }
   ],
   "source": [
    "s=(wine[:,-1]>7) & (wine[:,-2]>10)\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3d7f37e",
   "metadata": {},
   "source": [
    "22.\tChange the shape of wines array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "66a6538c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1599, 12)\n",
      "[[  7   0   0 ...   6   0   0]\n",
      " [  1   0  17 ...   3   0  26]\n",
      " [ 61   1   3 ...  42   0   3]\n",
      " ...\n",
      " [  2   0  23 ...   1   0   6]\n",
      " [ 25   0   3 ...  53   0   3]\n",
      " [666   9  30 ... 666  11  32]]\n"
     ]
    }
   ],
   "source": [
    "print(wine.shape)\n",
    "print(wine.reshape(12,1599))"
   ]
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
