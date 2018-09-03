import pandas as pd


class Cbs:
    """loads and munges projections data from cbssports.com"""

    def __init__(self):

        # map positions to cbs abbreviations
        self.pos = {'QB': 'QB', 'RB': 'RB', 'WR': 'WR', 'TE': 'TE', 'K': 'K', 'DEF': 'DST'}
        # Set cbs projections urls
        self.urlStart = 'http://www.cbssports.com/fantasy/football/stats/sortable/points/'
        self.urlEnd = '/standard/projections/2018/ytd?&print_rows=9999'

        self.teamMap = {'Texans': 'HOU', 'Seahawks': 'SEA', 'Packers': 'GB', 'Panthers': 'CAR', 'Patriots': 'NE',
                        'Eagles': 'PHI', 'Lions': 'DET', 'Falcons': 'ATL', '49ers': 'SF', 'Saints': 'NO',
                        'Colts': 'IND', 'Chiefs': 'KC', 'Raiders': 'OAK', 'Rams': 'LAR', 'Chargers': 'LAC',
                        'Steelers': 'PIT', 'Vikings': 'MIN', 'Cowboys': 'DAL', 'Bears': 'CHI', 'Titans': 'TEN',
                        'Redskins': 'WAS', 'Bengals': 'CIN', 'Broncos': 'DEN', 'Jaguars': 'JAX', 'Dolphins': 'MIA',
                        'Giants': 'NYG', 'Ravens': 'BAL', 'Buccaneers': 'TB', 'Bills': 'BUF',
                        'Browns': 'CLE', 'Jets': 'NYJ', 'Cardinals': 'ARI'}

        self.passerCols = ['Name', 'pass_att', 'pass_cmp', 'pass_yds', 'pass_td', 'intercept', 'rate', 'rush_att',
                           'rush_yds', 'rush_avg', 'rush_td', 'rec_tgt', 'recept', 'rec_yds', 'rec_avg', 'rec_td',
                           '2pt', 'fum_lost']

        self.kickerCols = ['Name', 'fg', 'fg_att', 'fg_lng', 'PAT_made', 'PAT_att', 'PAT_blckd', '1-19', '20-29',
                           '30-39', '40-49', '1-49', '50+']

    def defense(self, df):
        """Munges defense specific stats

        Args:
            df (dataframe): expect to receiving this from parsers function

        Returns:
            pandas DataFrame

        """
        # Change column names
        df.columns = ['Name', 'def_int', 'def_saftey', 'def_sk', 'tackles', 'fum_rec', 'forced_fumbles', 'def_td',
                      'pts_allowd', 'pass_yds_allowed', 'rush_yds_allowed', 'yds_allowed', 'FPTS']

        # Add missing columns
        df['itd'] = 0
        df['ftd'] = 0
        df['kick_rt_td'] = 0

        # remove the team from the name column
        df['Name'] = df['Name'].str.split(',').str[0]

        # Rearange cols
        cols = ['Name', 'def_int', 'def_saftey', 'def_sk', 'tackles', 'fum_rec',
                'forced_fumbles', 'def_td', 'itd', 'ftd', 'pts_allowd', 'pass_yds_allowed',
                'rush_yds_allowed', 'yds_allowed', 'kick_rt_td', 'FPTS']
        df = df[cols]

        # Finally drop the FPTS col we'll calculate it else where
        df = df.drop('FPTS', 1)

        # Map Team names to cities
        df['Name'] = df['Name'].map(self.teamMap)

        return df

    def parser(self, position):
        """Munges espn projections

        Args:
            position (str): QB, RB, WR, TE, K, DEF

        Returns:
            pandas DataFrame

        """
        url = self.urlStart + self.pos[position] + self.urlEnd

        # load url
        df = pd.read_html(url)[0]

        # Drop the first two rows of header info
        if position not in ('K', 'DEF'):
            df = df.loc[2:]
        else:
            df = df.loc[1:]

        # Make the real col index the first row
        df.columns = df.iloc[0]

        # drop the old first row and drop the old index column
        df = df.iloc[1:].reset_index().drop('index', 1)
        if position != 'DEF':

            # Rename columns
            if position != 'K':
                df.columns = ['Name', 'pass_att', 'pass_cmp', 'pass_yds', 'pass_td', 'intercept', 'rate', 'rush_att',
                              'rush_yds', 'rush_avg', 'rush_td', 'rec_tgt', 'recept', 'rec_yds', 'rec_avg', 'rec_td',
                              'fum_lost', 'FPTS']
                # add missing cols
                df['2pt'] = 0
                df = df.drop('FPTS', axis=1)
            else:
                df.columns = ['Name', 'fg', 'fg_att', 'fg_lng', 'PAT_made', 'PAT_att', 'PAT_blckd', 'FPTS']

            # Remove last row of non stats
            df = df[:-1]

            # new column with the team name split fom the name column
            df['tm'] = df['Name'].str.split(',').str[-1]
            df['tm'] = df['tm'].str.strip()
            df['tm'] = df['tm'].str.replace('JAC', 'JAX')

            # remove the team from the name column
            df['Name'] = df['Name'].str.split(',').str[0]

            # Normalize names
            df['Name'] = df['Name'].str.replace("'", '')
            df['Name'] = df['Name'].str.replace(".", '')
            df['Name'] = df['Name'].str.replace("-", '')
            df['Name'] = df['Name'].str.replace(" Jr", '')
            df['Name'] = df['Name'].str.replace(" Sr", '')
            df['Name'] = df['Name'].str.replace("*", '')

            # Combine team and name for final combined results
            df['Name'] = df['Name'] + " (" + df['tm'] + ")"

            # Move new team col to next to eh name col
            # put the final team column next to the player name
            if position != 'K':
                df = df[self.passerCols]
            if position == 'K':
                # add missing columns
                df['1-19'] = 0
                df['20-29'] = 0
                df['30-39'] = 0
                df['40-49'] = 0
                df['1-49'] = 0
                df['50+'] = 0

                df = df[self.kickerCols]

            # Convert everything from string to numeric
            return df
        else:
            return self.defense(df)