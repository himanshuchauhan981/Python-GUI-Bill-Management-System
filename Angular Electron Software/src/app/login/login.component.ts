import { AfterViewInit, Component, OnInit } from '@angular/core'
import { FormControl, FormGroup, Validators } from '@angular/forms'
import * as firebase from 'firebase'

import { UserService } from '../service/user.service'
import { AngularFireAuth } from '@angular/fire/auth'
import { credentials } from '../../environments/firebase_credentials'

@Component({
	selector: 'login',
	templateUrl: './login.component.html',
	styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit, AfterViewInit {

	constructor(private userService: UserService, private auth: AngularFireAuth) { }

	showPassword: boolean = false;

	hideEmailLogin: boolean = false;

	disableButton: boolean = true;

	windowRef: any;

	otpConfirmationDetails: any;

	loginForm = new FormGroup({
		username: new FormControl('', Validators.required)
	})

	otpForm = new FormGroup({
		otp: new FormControl('', Validators.required)
	})

	passwordForm = new FormGroup({
		password: new FormControl('', Validators.required)
	})

	get passwordFormControls() { return this.passwordForm.controls }

	get loginFormControls() { return this.loginForm.controls }

	get otpFormControls() { return this.otpForm.controls }

	ngOnInit() {
		this.windowRef = this.userService.windowRef;
		firebase.default.initializeApp(credentials)
	}

	ngAfterViewInit() {
		this.windowRef.recaptchaVerifier = new firebase.default.auth.RecaptchaVerifier('recaptcha-container', {
			'callback': (response) => {
				this.disableButton = false
			},
			'expired-callback': () => {
				this.disableButton = true
			}
		})
		this.windowRef.recaptchaVerifier.render()
	}



	showPasswordDialog() {
		let credentials: string = this.loginFormControls['username'].value;

		if (credentials.includes('@')) {
			this.showPassword = true;

		}
		else if (/^\d+$/.test(credentials)) {
			let appVerifier = this.windowRef.recaptchaVerifier;
			let mobileNumber: string = this.loginFormControls['username'].value;
			let loginType: string = 'verifyMobileNumber';
			this.signInWithMobileNumber(appVerifier, mobileNumber, loginType)
		}
		else {
			this.showPassword = false;

			this.loginFormControls['username'].setErrors({ 'incorrect': true })
		}
	}

	signInWithMobileNumber(appVerifier, mobileNumber: string, loginType: string) {
		firebase.default.auth().signInWithPhoneNumber(`+91${mobileNumber}`, appVerifier).then((result) => {
			this.showPassword = true;
			this.hideEmailLogin = true;
			this.otpConfirmationDetails = result;
		})
	}

	loginUser(form: FormGroup) {
		let username: string = this.loginFormControls['username'].value;
		let password = this.passwordFormControls['password'].value;
		let appVerifier = this.windowRef.recaptchaVerifier;
		let userData = {}

		// userData['loginType'] =  ? 'mobileNumber' : 'email'
		userData['appVerifier'] = appVerifier;
		userData['credentials'] = username;
		userData['password'] = password;

		if (form.valid) {
			if (/^\d+$/.test(username)) {
				let otp = this.otpFormControls['otp'].value;
				this.otpConfirmationDetails.confirm(otp).then(result => {
					console.log(result)
				})

			}
			// this.userService.loginUser(userData).subscribe(res => { })
		}

	}

}
