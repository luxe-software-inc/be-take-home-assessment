# Template for BE Take Home Assessment
We anticipate this test can take anywhere from 2.5 hours to 5 hours.

## First Time Setup
### Docker
For using this repository you will need to install Docker first

Use the [instructions here](https://docs.docker.com/get-docker/) to install docker

### Docker Build
To build the docker image for the project in the repository directory run

`docker build .`

This will create 2 images, 1 for the project code and another for the db

### Docker Compose Up
To run a docker container, in the repository directory run

`docker-compose up`

This will use the image from the docker build and run 2 containers. First container is the postgres db container,
and the 2nd container is your application.

The application container will run django app using wsgi on localhost:8000 port

(This step will also create migrations and apply them to postgres. A migration is a DDL command on a table structure)

### Run DB Seed (required 1 time only, and should fail after that)
This step is necessary to seed your postgres with data that we define for Django Model CustomerModel.py file 

The seed data lives in `movies/seed/0001_customer_seed.json`

We will exec into the running container created above with docker compose up and run the seed data loading to the db.

In a new terminal window navigate to the repository directory and then run:

` docker exec -it be-take-home-assessment-be-take-home-assessment-1 sh -c "python manage.py loaddata movies/seed/0001_customer_seed.json"`

### Testing the setup
While the docker-compose up command is still running, using your browser open
`http://localhost:8000/api/movies/customers/`

Note: To check what URLS are mapped to which views, please check all files called urls.py. All of the endpoints you create should be under the /api/ path 
If you see a Customer List with 2 rows Eddy / Chris then you have everything working correctly!

Now that the boring setup part is over, the fun part begins!

## Tasks
### Task 1 - Model Creation
We will create a Movie model and a wishlist model

1. In your browser open this url `https://apimocha.com/luxe-software-fe/get_movies`
2. Study the output, and make note of all differences in the field's output
3. We will create the MovieModel in `movies.models.movie_model.MovieModel` to store each field this api returned
4. We will create another WishlistModel in `movies.models.wishlist_model.WishlistModel` which will store a customers's wishlisted (read select) movies. It should have a customer_id & movie_id that are foreign keys to CustomerModel and MovieModel respectively

### Task 2 - Add Serializers
We will create serializers for the models defined above.

1. Create the `MovieSerializer` in `movies.serializers.movie_serializer`
2. Create the `WishlistSerializer` in `movies.serializers.wishlist_serializer`

### Task 3 - Movies API
In this task, we will create 2 rest endpoints for the Movie Model to load the ApiMocha api into the movie model table, and second one will return the list of all movies in the table

First API
1. Create an API which gets the data from apimocha.com api and creates ("seeds") movies in the movie model table  
2. The api should live in `movies.views.movie_view.MovieView`
3. In `movies.urls` add the path as `localhost:8000/api/movies/movie/load_external_data/` (its ok to be a GET or POST)
4. Add code to call the apimocha.com url (requests package is already installed if you wish to use it) and create new rows in Movie.Model. This code can be added wherever you feel is the cleanest

Second API
1. Create a new api which will return a JSON list of all movies
2. The api should live in `movies.views.movie_view.MovieView`
3. In `movies.urls` add the path as GET `localhost:8000/api/movies/movie/`
4. Add code to return JSON list of all movies in the database after the previous api has been called at least once. This code can be added wherever you feel is the cleanest

(If your second API does not return any movies, it's likely your first api didn't work correctly or you never opened first api in your browser to trigger the "seed" (data loading) for movie model)

### Task 4 - Wishlist API
In this task we will create 2 api's for wishlist model. One to add a movie to a customers wishlist, and second to get all wishlist movies for a given customer

First API
1. Create an api that will allow a customer to add a movie to their wishlist
2. The api should live in `movies.views.wishlist_view.WishlistView`
3. In `movies.urls` add a path for POST `localhost:8000/api/movies/wishlist/`
4. Add code to add a new wishlist model table row for the customer and for the movie they selected. This code can be added wherever you feel is the cleanest

Second API
1. Create a new api that will return all wishlisted movies of a customer
2. The api should live in `movies.views.wishlist_view.WishlistView`
3. In `movies.urls` add a path for GET `localhost:8000/api/movies/wishlist/all_movies/<YOUR_DEFINED_PATH>`
4. Add code to return a JSON list of wishlisted movies of the customer (Should this return a list of wishlistModel or movieModel?)

### Task 5 - Submit your take home assessment
1. Clone the repository to your local machine by using `git clone <git_repo_path_from_git_hub>` in your terminal
2. Next create a new branch in your terminal with `git checkout -b <your_name>_take_home_submission`
3. After making the code changes + testing them, commit your changes using `git add . && git commit -m "Take home assignment submission"`
4. Next push your changes to Github using `git push origin <your_name>_take_home_submission`
5. [Optional] on Github UI create a pull request between main branch and your branch
6. [Optional] Send a reply to the email that you used to schedule accessing this repo
7. We will follow up within 2 days after this for the next steps!

## Completion!

In total by the end of this you would have based on how you implement the following things
1. 2 Django Models --> MovieModel & WishlistModel
2. 2 Django Serializers --> MovieSerializer & WishlistSerializer
3. 2 Movie APIs --> Load movie data from external API + get a list of all movies
4. 2 Wishlist APIs --> Create a new wishlist movie for a customer + return all wishlisted movies for a customer

This concludes the features you need to build for this take home assessment!
From our side, we would like to thank you for taking the time doing this! Once you submit this, we will strive to get back within 24 hours.

We would also love to hear your feedback on this take home assignment! Do you think something was missing, or was not clear or anyway we can improve this or
just to send a shout-out we would love to hear that through email here: recruitment_feedback@luxesoftware.com

## FAQs
1. Can I access the postgres db running to run sql commands?
Yes! Run command `docker exec -it be-take-home-assessment-be-take-home-db-1 psql -U devuser devdb`
PS: `docker compose up` should be running in another window
2. How do I see all of the tables in psql shell in #1?
Here is a [CheatSheet](https://postgrescheatsheet.com) which covers this. \dt and \d are the most useful and \q is to exit pqsl.
3. What are my models name is as a table in psql?
Its `movies_<model_name_with_underscores>` for eg `movies_customermodel` or `movies_moviemodel` or `movies_wishlistmodel`
4. While running `docker exec ...` I got an error `Error response from daemon: Container XXXXX is not running`
You don't have `docker-compose up` running in a different terminal. Exec runs the command on existing running container which should be `running`. You can use docker run instead if you would like but then you need to tag the image name using `docker build -t be-take-home`
5. Can I get sh / bash terminal in the running containers?
Yes! Just run `docker exec -it be-take-home-assessment-be-take-home-assessment-1 sh`
6. Where are you making migrations and running migrations?
That happens in the `docker-compose.yml` file command. If you suspect your changes in the model are not being migrated (applied) you can manually run them with `docker exec` as well
7. I had an error from the postgres db container.
Email [amiraj@luxesoftware.com](mailto:amiraj@luxesoftware.com). You might have a package issue.
8. I had an error from docker.
Email [amiraj@luxesoftware.com](mailto:amiraj@luxesoftware.com). You might have a package issue.
9. Should I give up the test if I have taken more than 2.5 hours already?
Definitely NOT! Its an estimate for a reason. As we use this problem more and more we would have a better sense of time commitment required for this test. Please bear with us since it might be impossible to finish this within 2.5 hours lowest estimate.
10. What to do if I just am unable to seed the data and want to quit?
You don't necessarily need this data. If you are unable to seed the data, just assume customer id will be 100 for the wishlist. Although not fully complete, its better than seeding data :)
11. Is there something weird with the API Mocha returning data for fields Production or DVD?
That is intentional, and not a mistake in the API response.

### Best of Luck!
Hope you had fun while working through this! If you did not, or it took you more than 2 hours please shoot some feedback at recruitment_feedback@luxesoftware.com to help us make this more streamlined!