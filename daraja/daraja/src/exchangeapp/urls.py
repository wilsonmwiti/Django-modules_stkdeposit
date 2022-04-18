from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import Settings


urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('login',views.login,name="login"),

    path('login/<str:promo>/login/',views.login, name="login"),

    path('register',views.register,name="register"),
    path('register/<str:i_link>/',views.register, name="register"),
    path('register/<str:i_link>/login/',views.login2, name="login"),
    path('register/<str:i_link>/login/register/',views.register, name="login"),
    path('register/<str:i_link>/login/login',views.login2, name="login"),

    path('dashboard',views.dashboard,name="dashboard"),
    path('dashboard2',views.dashboard2,name="dashboard2"),
    path('deposit',views.deposit,name="depoit"),
    path('v_code',views.v_code,name="v_code"),
    path('withdraw',views.withdraw,name="withdraw"),
    path('buy_share',views.buy_share,name="buy_share"),
    path('sell_share',views.sell_share,name="sell_share"),
    path('logout',views.logout,name="logout"),
    path('resend_code',views.resend_code,name="resend_code"),
    path('edit_phone',views.edit_phone,name="edit_phone"),
    path('wallet',views.wallet,name="wallet"),
    path('previous',views.previous,name="previous"),
    path('loans',views.loans,name="loans"),
    path('i_list',views.i_list,name="i_list"),
    path('profile',views.profile,name="profile"),
    path('depositn',views.depositn,name="deposit"),
    path('profile',views.profile,name="profile"),
    path('change_password',views.change_password, name="change_password"),
    path('transaction',views.transaction,name="transaction"),
    path('s_login',views.s_login, name="s_login"),
    path('staff_dashboard',views.staff_dashboard, name="staff_dashboard"),
    path('refund',views.refund, name="refund"),
    path('pay_refund',views.pay_refund, name="pay_refund"),
    path('deposit22',views.deposit22, name="depositw32"),
    path('search_d',views.search_d, name="search_d"),
   



    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name="password_reset"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),


]
