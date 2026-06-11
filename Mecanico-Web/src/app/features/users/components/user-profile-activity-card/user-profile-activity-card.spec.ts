import { ComponentFixture, TestBed } from "@angular/core/testing";

import { UserProfileActivityCard } from "./user-profile-activity-card";

describe("UserProfileActivityCard", () => {
	let component: UserProfileActivityCard;
	let fixture: ComponentFixture<UserProfileActivityCard>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [UserProfileActivityCard],
		}).compileComponents();

		fixture = TestBed.createComponent(UserProfileActivityCard);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
