class Date
{
    public:         // 公用界面
        enum Month{jan=1, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec};
        class Bad_date{ };   // 异常类
        Date(int dd=0, Month mm=Month(0), int yy=0);  // 0表示取默认值

        // 检查Date的函数
        int day() const;
        Month month() const;
        int year() const;
        string string_rep() const;      // 字符串表示
        void char_rep(char s[]) const;  // c风格字符串

        static void set_default(int, Month, int);

        // 修改Date 的函数
        Date& add_year(int n);
        Date& add_month(int n);
        Date& add_may(int n);

    private:
        int d, m, y;
        static Date default_date;
};

Date::Date(int dd, Month mm, int yy)
{
    if (yy == 0)
        yy = default_date.year();
    if (mm == 0)
        mm = default_date.month();
    if (dd == 0)
        dd = default_date.day();

    int max;

    switch (mm)
    {
        case feb:
            max = 28 + leapyear(yy);
            break;
            
        case apr:
        case jun:
        case sep:
        case nov:
            max = 30;
            break;

        case Jan:
        case mar:
        case may:
        case jul:
        case aug:
        case oct:
        case dec:
            max = 31;
            break;

        default:
            throw Bad_date();   // 有人捣乱
    }

    if (dd<1 || max<dd)
        throw Bad_date();

    y = yy;
    m = mm;
    d = dd;
}

inline int Date::day() const
{
    return d;
}
Date& Date::add_month(int n)
{
    if (n == 0)
        return *this;
    if (n > 0)
    {
        int delta_y = n / 12;
        int mm = m + n%12;
        if (12 < mm)            // 注意：int(dec) = 12
        {
            delta_y++;
            mm -= 12;
        }
        // 处理Month(mm)没有天数d的情况
        y += delta_y;
        m = Month(mm);
        return *this;
    }
    // 处理负数n
    return *this;
}

inline bool operator==(Date a, Date b)
{
    return a.day() == b.day() && a.month() == b.month() && a.year() == b.year();
}

