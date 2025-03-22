const passport = require("passport");
const LocalStrategy = require("passport-local").Strategy;
const GitHubStrategy = require("passport-github2").Strategy
const userController = require("../controllers/userController");

const githublogin = new GitHubStrategy({
  clientID: "Ov23liiKQ7WkJrBXYgRc",
  clientSecret: "19fe2afb28b2f2e351c4a04a353565a867677f50",
  callbackURL: "http://localhost:8000/auth/github/callback"
  },
  function(accessToken, refreshToken, profile, done) {
    const user = database.find((user) => user.id === profile.id)
    if(user){
      return done(err, user);
    }
    else{
      const newUser = {
        id: profile.id,
        name: profile.displayName
      }
      database.push(newUser)
    }
  }
);

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

passport.serializeUser(function (user, done) {
  done(null, user.id);
});

passport.deserializeUser(function (id, done) {
  let user = userController.getUserById(id);
  if (user) {
    done(null, user);
  } else {
    done({ message: "User not found" }, null);
  }
});

module.exports = passport.use(localLogin).use(githublogin);
