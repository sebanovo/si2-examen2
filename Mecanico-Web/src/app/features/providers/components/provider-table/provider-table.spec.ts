import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ProviderTable } from "./provider-table";

describe("ProviderTable", () => {
	let component: ProviderTable;
	let fixture: ComponentFixture<ProviderTable>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ProviderTable],
		}).compileComponents();

		fixture = TestBed.createComponent(ProviderTable);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
