const express = require('express');
const passport = require('../middleware/passport');
const { forwardAuthenticated, isAdmin } = require('../middleware/checkAuth');

const router = express.Router();

router.get('/login', forwardAuthenticated, (req, res) => res.render('login'));

router.post('/login', passport.authenticate('local'), (req, res) => {
  if (req.user && req.user.role === 'admin') {
    return res.redirect('/admin');
  } else if (req.user && req.user.role === 'user') {
    return res.redirect('/dashboard');
  } else {
    res.redirect('/auth/login');
  }
});

router.get(
  '/github',
  passport.authenticate('github', { scope: ['user:email'] })
);

router.get(
  '/github/callback',
  passport.authenticate('github', {
    successRedirect: '/dashboard',
    failureRedirect: '/auth/login',
  })
);

router.post('/revoke', (req, res) => {
  req.logout();
  req.session.destroy((err) => {
    res.clearCookie('connect.sid');
   
    res.redirect("/auth/login")
  });
});


router.get('/logout', (req, res, next) => {
  req.logout();
  req.session.destroy((err) => {
    if (err) return next(err);
    res.clearCookie('connect.sid');
    res.redirect('/auth/login');
  });
});

module.exports = router;
