USE baseball
SELECT YEAR(Date) as Year, AVG(Attendance) as Total_Attendance
FROM dbo.GameLogsMNOnly
GROUP BY YEAR(Date)
ORDER BY YEAR(Date);

USE baseball
SELECT HomeTeam, YEAR(Date) as Year, AVG(Attendance) as Total_Attendance
FROM dbo.GameLogsNewNoDupes
WHERE Hometeam NOT IN ('MIN')
GROUP BY HomeTeam, YEAR(Date)
ORDER BY Hometeam, YEAR(Date);
