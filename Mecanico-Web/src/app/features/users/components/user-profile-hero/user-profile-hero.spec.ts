import { ComponentFixture, TestBed } from "@angular/core/testing";

import { UserProfileHero } from "./user-profile-hero";

describe("UserProfileHero", () => {
	let component: UserProfileHero;
	let fixture: ComponentFixture<UserProfileHero>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [UserProfileHero],
		}).compileComponents();

		fixture = TestBed.createComponent(UserProfileHero);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
