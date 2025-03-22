const passport = require("passport");
const LocalStrategy = require("passport-local").Strategy;
const GitHubStrategy = require("passport-github2").Strategy;
const userController = require("../controllers/userController");
require('dotenv').config();


const localLogin = new LocalStrategy(
  {
    usernameField: "email",
    passwordField: "password",
  },
  (email, password, done) => {
    const user = userController.getUserByEmailIdAndPassword(email, password);
    return user
      ? done(null, user)
      : done(null, false, {
          message: "Your login details are not valid. Please try again",
        });
  }
);


const github = new GitHubStrategy(
  {
    clientID: process.env.GITHUB_CLIENT_ID,
    clientSecret: process.env.GITHUB_CLIENT_SECRET,
    callbackURL: "http://localhost:8000/auth/github/callback" 
  },
  function(accessToken, refreshToken, profile, done) {
   
    return done(null, profile);
  }
)

passport.serializeUser((user, done) => {
  if (user && user.provider === 'github') {
    done(null, user);
  } else {
    done(null, user.id);
  }
});

passport.deserializeUser((sessionData, done) => {
  if (sessionData && sessionData.provider === 'github') {
    return done(null, sessionData);
  }
  const user = userController.getUserById(sessionData);
  if (user) {
    return done(null, user);
  }
  done(new Error("User not found"), null);
});


passport.use(localLogin);
passport.use(github);

module.exports = passport;
