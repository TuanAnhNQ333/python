#include <stdio.h>
int main()
{
    int c;
    int check ;// 0 : ky tu in ra binh thuong
               // 1 : ky tu truoc la ky tu trang

    while ((c = getchar()) != -1)
    {
        if(c == '.' )

       break;
    if(c == ' ')
       check ++;
    else check = 0;

    if (check <= 1)
       putchar(c);
    

}
return 0;
}
