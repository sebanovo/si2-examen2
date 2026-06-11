import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ServiceTable } from "./service-table";

describe("ServiceTable", () => {
	let component: ServiceTable;
	let fixture: ComponentFixture<ServiceTable>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ServiceTable],
		}).compileComponents();

		fixture = TestBed.createComponent(ServiceTable);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
