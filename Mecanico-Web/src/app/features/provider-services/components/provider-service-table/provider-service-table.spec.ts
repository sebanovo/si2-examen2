import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ProviderServiceTable } from "./provider-service-table";

describe("ProviderServiceTable", () => {
	let component: ProviderServiceTable;
	let fixture: ComponentFixture<ProviderServiceTable>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ProviderServiceTable],
		}).compileComponents();

		fixture = TestBed.createComponent(ProviderServiceTable);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
