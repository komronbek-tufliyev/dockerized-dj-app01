-- Database initialisation procedure. Passwords are changed over during the manual setup
-- phase and are only here to serve as placeholders for user initialisation.

-- Alter the default postgres user to have an encrypted password
ALTER USER postgres WITH ENCRYPTED PASSWORD 'dj@n+Go!';

-- Create a new superuser with an encrypted password
CREATE USER archer WITH SUPERUSER ENCRYPTED PASSWORD 'dj@n+Go!user';

-- Make the password valid forever
ALTER USER archer VALID UNTIL 'infinity';

-- Create the initial database and assign ownership to new user
CREATE DATABASE demodb OWNER archer;

-- Grant all rights and priviliges to the newly created database to the newly created superuser
GRANT ALL PRIVILEGES ON DATABASE demodb TO archer;