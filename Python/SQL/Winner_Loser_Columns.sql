DECLARE @HomeTeamScore int = 0;
DECLARE @VisitingTeamScore int = 0;
DECLARE @HomeTeam varchar(50);
DECLARE @VisitingTeam varchar(50);
DECLARE @Count BIGINT = 1;
DECLARE @MaxSize BIGINT = 0;

SELECT @MaxSize = COUNT(0) FROM dbo.GameLogsNewNoDupes;

WHILE @Count <= @MaxSize
BEGIN
	SET @HomeTeamScore = (SELECT CAST(HomeTeamScore AS INT) FROM dbo.GameLogsNewNoDupes WHERE GameID = @Count)
	SET @VisitingTeamScore = (SELECT CAST(VistingTeamScore AS INT) FROM dbo.GameLogsNewNoDupes WHERE GameID = @Count)
	SET @HomeTeam = (SELECT HomeTeam FROM dbo.GameLogsNewNoDupes WHERE GameID = @Count)
	SET @VisitingTeam = (SELECT VisitingTeam FROM dbo.GameLogsNewNoDupes WHERE GameID = @Count)

	IF @HomeTeamScore > @VisitingTeamScore
	BEGIN
		UPDATE dbo.GameLogsNewNoDupes SET winner = @HomeTeam, loser = @VisitingTeam
		WHERE GameID = @Count
	END
	ELSE
	BEGIN
		UPDATE dbo.GameLogsNewNoDupes SET winner = @VisitingTeam, loser = @HomeTeam
		WHERE GameID = @Count
	END
	SET @Count = @Count + 1
END
