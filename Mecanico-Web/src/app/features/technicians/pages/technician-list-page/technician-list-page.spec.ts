import { ComponentFixture, TestBed } from "@angular/core/testing";

import { TechnicianListPage } from "./technician-list-page";

describe("TechnicianListPage", () => {
	let component: TechnicianListPage;
	let fixture: ComponentFixture<TechnicianListPage>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [TechnicianListPage],
		}).compileComponents();

		fixture = TestBed.createComponent(TechnicianListPage);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
