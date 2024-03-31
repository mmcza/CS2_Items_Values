# Get and save Counter-Strike 2 cases and capsules prices

This is a simple web scraper that gets the prices of the cases and capsules of Counter-Strike 2 from the Steam Community Market.

> [!NOTE]
> Please note that this is a personal project and is not intended to be used for commercial purposes.

The data is saved to PostgreSQL database and in future I will add a simple web interface to display the data (hopefully). I also added that the recent data is being saved as JSON to a .txt file, but I will probably remove that in the future.

More about the database schema can be found in the wiki (once I create it).

## Result example

![Example](/pictures/cs2_cases_db.png)

To save space all cases get their id (they are created when the script runs for the first time or when a new case is added to the game) that is saved in the `cases_list` table. Timestamp of each search and currency of the price is saved in the `searches` table. In the `containers` table there are all the prices, amount of listings, search_id and case id of the cases and capsules.

This allows to easily track the price changes of the cases and capsules. 

## How to run

To run the project you need to install the requirements from the `requirements.txt` file and create a PostgreSQL database. You can make the script run periodically by using a cron job or a task scheduler.